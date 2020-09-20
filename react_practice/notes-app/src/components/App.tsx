import React from "react";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import Header from "./Header";
import Footer from "./Footer";
import Notespage from "./Notespage";
import Mainform from "./loging_files/Mainform";
import About from "./About";
import "../../node_modules/bootstrap/dist/css/bootstrap.min.css";

function App() {
  return (
    <div>
      <Header />
      <Router>
        <div>
          <nav className="navbar navbar-expand-lg navbar-light bg-light">
            <a className="navbar-brand" href="#">
              Navbar
            </a>
            <button
              className="navbar-toggler"
              type="button"
              data-toggle="collapse"
              data-target="#navbarNavAltMarkup"
              aria-controls="navbarNavAltMarkup"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <span className="navbar-toggler-icon"></span>
            </button>
            <ul className="navbar-nav mr-auto" id="navbarNavAltMarkup">
              <li className="nav-link">
                <Link to="/">Notes editing</Link>
              </li>
              <li className="nav-item nav-link">
                <Link to="/about">About</Link>
              </li>
              <li className="nav-item nav-link">
                <Link to="/register">Registration</Link>
              </li>
            </ul>
            <hr />
          </nav>

          {/* A <Switch> looks through its children <Route>s and
            renders the first one that matches the current URL. */}
          <Switch>
            <Route path="/about">
              <About />
            </Route>
            <Route path="/register">
              <Mainform />
            </Route>
            <Route path="/">
              <Notespage />
            </Route>
          </Switch>
        </div>
      </Router>
      <Footer />
    </div>
  );
}
export default App;