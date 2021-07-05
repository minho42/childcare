import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import ChildcareList from "./components/ChildcareList";
import About from "./components/About";

function App() {
  return (
    <div className="text-gray-800">
      <Router>
        <Navbar />
        <Switch>
          <Route exact path="/">
            <ChildcareList />
          </Route>
          <Route exact path="/about">
            <About />
          </Route>
        </Switch>
      </Router>
    </div>
  );
}

export default App;
