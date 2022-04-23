import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import ChildcareList from "./components/ChildcareList";
import About from "./components/About";

function App() {
  return (
    <div className="text-gray-800">
      <Router>
        <Navbar />
        <Routes>
          <Route path="/" element={<ChildcareList />} />
          <Route path="/about" element={<About />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
