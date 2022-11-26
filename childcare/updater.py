import csv
import re
from datetime import timedelta
from pathlib import Path
from typing import Dict, List

import requests
from core.utils import random_useragent, started_and_finished, timeit
from django.utils import timezone

from .models import Childcare

CSV_FILE_NAME = "data.csv"


class Updater:
    def __init__(self):
        self.user_agent = random_useragent()

    def _ratingToNumber(self, r: str) -> int:
        r = r.strip().lower()
        if r.startswith("s"):
            return 1
        elif r.startswith("w"):
            return 2
        elif r.startswith("m"):
            return 3
        elif r.startswith("exceed"):
            return 4
        elif r.startswith("excel"):
            return 5
        return 0

    def _is_csv_old(self) -> bool:
        try:
            last_modified = Childcare.objects.order_by("-modified").first().modified
            if last_modified + timedelta(hours=48) < timezone.now():
                return True
            return False
        except:
            return True

    @timeit
    def _get_new_count_for_nsw(self) -> int:
        count = 0
        url = "https://www.acecqa.gov.au/resources/national-registers/services?s=&f%5B0%5D=service_state%3ANSW"
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-language": "en-AU,en;q=0.9,ko-KR;q=0.8,ko;q=0.7,en-GB;q=0.6,en-US;q=0.5",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            # "referrerPolicy": "strict-origin-when-cross-origin",
            # "body": "null",
            # "method": "GET",
            # "mode": "cors",
            # "credentials": "omit",
            "user-agent": self.user_agent,
        }
        s = requests.session()
        r = s.get(url, headers=headers)
        try:
            count = re.findall(r"Found ([\d,]+)", r.text)[0]
            count = int(count)
        except (IndexError, ValueError) as e:
            count = 0
        return count

    @timeit
    def _get_new_count_for_all(self) -> int:
        count = 0
        url = "https://www.acecqa.gov.au/resources/national-registers/services?s=&field_service_id="
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-language": "en-AU,en;q=0.9,ko-KR;q=0.8,ko;q=0.7,en-GB;q=0.6,en-US;q=0.5",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "referrer": "https://www.acecqa.gov.au/resources/national-registers",
            # "referrerPolicy": "strict-origin-when-cross-origin",
            # "body": "null",
            # "method": "GET",
            # "mode": "cors",
            # "credentials": "omit",
            "user-agent": self.user_agent,
        }
        s = requests.session()
        r = s.get(url, headers=headers)
        try:
            count = re.findall(r"Found ([\d,]+)", r.text)[0]
            count = int(count)
        except (IndexError, ValueError) as e:
            count = 0
        return count

    def _is_total_count_different(self) -> bool:
        current_count = Childcare.objects.count()
        if not current_count:
            return True

        # new_count = self._get_new_count_for_all()
        new_count = self._get_new_count_for_nsw()
        print(f"current_count: {current_count}")
        print(f"new_count: {new_count}")
        return current_count != new_count

    def _is_csv_to_be_updated(self) -> bool:
        if self._is_csv_old() or self._is_total_count_different():
            return True
        return False

    @started_and_finished
    @timeit
    def _download_csv_for_nsw(self) -> None:
        url = "https://www.acecqa.gov.au/sites/default/files/national-registers/services/Education-services-nsw-export.csv"
        s = requests.session()
        r = s.get(url)
        print(r.status_code)
        with open(CSV_FILE_NAME, "wb") as file:
            file.write(r.content)

    @started_and_finished
    @timeit
    def _download_csv_for_all(self) -> None:
        url = "https://www.acecqa.gov.au/sites/default/files/national-registers/services/Education-services-au-export.csv"
        s = requests.session()
        r = s.get(url)
        print(r.status_code)
        with open(CSV_FILE_NAME, "wb") as file:
            file.write(r.content)

    @started_and_finished
    @timeit
    def _delete_no_longer_exist(self) -> None:
        column_names_and_indexes = self._get_column_index_for_fields()
        new_approval_numbers = []
        with open(CSV_FILE_NAME, newline="") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                new_approval_numbers.append(row[column_names_and_indexes[self._index_for_field("approval_number")]])

        approval_numbers_to_be_deleted = []
        for c in Childcare.objects.all():
            if c.approval_number not in new_approval_numbers:
                approval_numbers_to_be_deleted.append(c.approval_number)
        print("approval_numbers_to_be_deleted")
        print(approval_numbers_to_be_deleted)
        # TODO delete approval_numbers_to_be_deleted
        for approval_number in approval_numbers_to_be_deleted:
            try:
                obj = Childcare.objects.get(approval_number=approval_number)
                obj.delete()
            except Childcare.DoesNotExist:
                pass

    def _get_csv_header(self) -> List:
        header = []
        with open(CSV_FILE_NAME, newline="") as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)
        return header

    def _index_for_field(self, name: str) -> int:
        csv_name_to_model_name = {
            "approval_number": "ServiceApprovalNumber",
            "name": "ServiceName",
            "address": "ServiceAddress",
            "suburb": "Suburb",
            "state": "State",
            "postcode": "Postcode",
            "rating1": "QualityArea1Rating",
            "rating2": "QualityArea2Rating",
            "rating3": "QualityArea3Rating",
            "rating4": "QualityArea4Rating",
            "rating5": "QualityArea5Rating",
            "rating6": "QualityArea6Rating",
            "rating7": "QualityArea7Rating",
            "overall_rating": "OverallRating",
            "ratings_issued": "RatingsIssued",
            "prev_rating1": "PreviousQualityArea1Rating",
            "prev_rating2": "PreviousQualityArea2Rating",
            "prev_rating3": "PreviousQualityArea3Rating",
            "prev_rating4": "PreviousQualityArea4Rating",
            "prev_rating5": "PreviousQualityArea5Rating",
            "prev_rating6": "PreviousQualityArea6Rating",
            "prev_rating7": "PreviousQualityArea7Rating",
            "prev_overall_rating": "PreviousOverallRating",
            "prev_ratings_issued": "PreviousRatingsIssued",
        }
        return csv_name_to_model_name[name]

    def _get_column_index_for_fields(self) -> Dict[str, int]:
        header = self._get_csv_header()
        # print(header)
        column_names_and_indexes = {}
        column_names = [
            "ServiceApprovalNumber",
            "ServiceName",
            "ServiceAddress",
            "Suburb",
            "State",
            "Postcode",
            "QualityArea1Rating",
            "QualityArea2Rating",
            "QualityArea3Rating",
            "QualityArea4Rating",
            "QualityArea5Rating",
            "QualityArea6Rating",
            "QualityArea7Rating",
            "OverallRating",
            "RatingsIssued",
            "PreviousQualityArea1Rating",
            "PreviousQualityArea2Rating",
            "PreviousQualityArea3Rating",
            "PreviousQualityArea4Rating",
            "PreviousQualityArea5Rating",
            "PreviousQualityArea6Rating",
            "PreviousQualityArea7Rating",
            "PreviousOverallRating",
            "PreviousRatingsIssued",
        ]
        for name in column_names:
            # print(name, header.index(name))
            column_names_and_indexes.update({name: header.index(name)})
        return column_names_and_indexes

    @started_and_finished
    @timeit
    def update(self) -> None:
        if not self._is_csv_to_be_updated():
            print("No need to update CSV")
            return

        print("Need to update CSV")
        # self._download_csv_for_all()
        self._download_csv_for_nsw()

        if not Path(CSV_FILE_NAME).is_file():
            print("Something wrong! csv not exist")
            return

        self._delete_no_longer_exist()

        column_names_and_indexes = self._get_column_index_for_fields()
        # print(column_names_and_indexes)

        print("Upsert started")
        with open(CSV_FILE_NAME, newline="") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                approval_number = row[column_names_and_indexes[self._index_for_field("approval_number")]]
                name = row[column_names_and_indexes[self._index_for_field("name")]]
                address = row[column_names_and_indexes[self._index_for_field("address")]]
                suburb = row[column_names_and_indexes[self._index_for_field("suburb")]]
                state = row[column_names_and_indexes[self._index_for_field("state")]]
                postcode = row[column_names_and_indexes[self._index_for_field("postcode")]]

                rating1 = self._ratingToNumber(row[column_names_and_indexes[self._index_for_field("rating1")]])
                rating2 = self._ratingToNumber(row[column_names_and_indexes[self._index_for_field("rating2")]])
                rating3 = self._ratingToNumber(row[column_names_and_indexes[self._index_for_field("rating3")]])
                rating4 = self._ratingToNumber(row[column_names_and_indexes[self._index_for_field("rating4")]])
                rating5 = self._ratingToNumber(row[column_names_and_indexes[self._index_for_field("rating5")]])
                rating6 = self._ratingToNumber(row[column_names_and_indexes[self._index_for_field("rating6")]])
                rating7 = self._ratingToNumber(row[column_names_and_indexes[self._index_for_field("rating7")]])
                ratings = [rating1, rating2, rating3, rating4, rating5, rating6, rating7]
                try:
                    average_ratings = round(sum(ratings) / len(ratings), 1)
                except TypeError:
                    average_ratings = 0
                overall_rating = row[column_names_and_indexes[self._index_for_field("overall_rating")]]
                overall_rating_number = self._ratingToNumber(overall_rating)
                ratings_issued = row[column_names_and_indexes[self._index_for_field("ratings_issued")]]

                prev_rating1 = self._ratingToNumber(
                    row[column_names_and_indexes[self._index_for_field("prev_rating1")]]
                )
                prev_rating2 = self._ratingToNumber(
                    row[column_names_and_indexes[self._index_for_field("prev_rating2")]]
                )
                prev_rating3 = self._ratingToNumber(
                    row[column_names_and_indexes[self._index_for_field("prev_rating3")]]
                )
                prev_rating4 = self._ratingToNumber(
                    row[column_names_and_indexes[self._index_for_field("prev_rating4")]]
                )
                prev_rating5 = self._ratingToNumber(
                    row[column_names_and_indexes[self._index_for_field("prev_rating5")]]
                )
                prev_rating6 = self._ratingToNumber(
                    row[column_names_and_indexes[self._index_for_field("prev_rating6")]]
                )
                prev_rating7 = self._ratingToNumber(
                    row[column_names_and_indexes[self._index_for_field("prev_rating7")]]
                )
                prev_ratings = [
                    prev_rating1,
                    prev_rating2,
                    prev_rating3,
                    prev_rating4,
                    prev_rating5,
                    prev_rating6,
                    prev_rating7,
                ]
                try:
                    prev_average_ratings = round(sum(prev_ratings) / len(prev_ratings), 1)
                except TypeError:
                    prev_average_ratings = 0
                prev_overall_rating = row[column_names_and_indexes[self._index_for_field("prev_overall_rating")]]
                prev_overall_rating_number = self._ratingToNumber(prev_overall_rating)
                prev_ratings_issued = row[column_names_and_indexes[self._index_for_field("prev_ratings_issued")]]

                c, created = Childcare.objects.update_or_create(
                    approval_number=approval_number,
                    defaults={
                        "approval_number": approval_number,
                        "name": name,
                        "address": address,
                        "suburb": suburb,
                        "state": state,
                        "postcode": postcode,
                        "rating1": rating1,
                        "rating2": rating2,
                        "rating3": rating3,
                        "rating4": rating4,
                        "rating5": rating5,
                        "rating6": rating6,
                        "rating7": rating7,
                        "average_ratings": average_ratings,
                        "overall_rating": overall_rating,
                        "overall_rating_number": overall_rating_number,
                        "ratings_issued": ratings_issued,
                        "prev_rating1": prev_rating1,
                        "prev_rating2": prev_rating2,
                        "prev_rating3": prev_rating3,
                        "prev_rating4": prev_rating4,
                        "prev_rating5": prev_rating5,
                        "prev_rating6": prev_rating6,
                        "prev_rating7": prev_rating7,
                        "prev_average_ratings": prev_average_ratings,
                        "prev_overall_rating": prev_overall_rating,
                        "prev_overall_rating_number": prev_overall_rating_number,
                        "prev_ratings_issued": prev_ratings_issued,
                        "modified": timezone.now(),
                    },
                )
                if created:
                    print(f"Created: {approval_number}, {name}")
                # print(name)
