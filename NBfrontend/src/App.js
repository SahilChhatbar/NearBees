import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Button } from 'react-bootstrap';
import { Carousel } from 'react-responsive-carousel';
import 'react-responsive-carousel/lib/styles/carousel.min.css';
import './App.css';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import GS from './GettingStart/GS'; 
import Guide from './Guide/Guide';

function App() {
  return (
    <Router>
      <div className="App">
        <Header />
        <Routes>
          <Route path="/" element={<MainContent />} />
          <Route path="/gs" element={<GS />} />
          <Route path="/guide" element={<Guide />} />
        </Routes>
      </div>
    </Router>
  );
}

function Header() {
  return (
    <header className="App-header">
      <img className="logo" src="NearBees.png" alt='NearBees' />
    </header>
  );
}

function MainContent() {
  return (
    <div className="container mt-4">
      <div className="overlay"></div>
      <div className="overlay-content">
        <div className="row">
          <div className="col-md-3">
            <div className="page">
              <h3>Getting Started</h3>
              <p>Learn how to use NearBees for flower recognition.</p>
              <Link to="/gs" className="btn btn-primary btn-go-to">Go To Section</Link>
            </div>
          </div>
          <div className="col-md-6">
            <CarouselComponent />
          </div>
          <div className="col-md-3">
            <div className="page">
              <h3>Guide</h3>
              <p>Find detailed guides and FAQs about using NearBees.</p>
              <Link to="/guide" className="btn btn-primary btn-go-to"> Go To Section</Link>
            </div>
          </div>
        </div>
        <h2 className="mt-4">Identify the Flower</h2>
        <div className="upload-container">
          <Button variant="warning" size="lg" onClick={() => window.location.href = 'http://localhost:8000/'}>
  Upload Photo
</Button>

        </div>
      </div>
    </div>
  );
}

function CarouselComponent() {
  return (
    <div className="carousel-container">
      <Carousel showThumbs={false} dynamicHeight={false} showStatus={false} autoPlay={true} infiniteLoop={true} interval={2500} autoFocus={true}>
        <div>
          <img src="https://i0.wp.com/palatineroses.com/wp-content/uploads/2021/03/rosemantic-red-huge.jpg?fit=1774%2C1331&ssl=1" alt="Flower 1" />
          <p className="legend">Rose</p>
        </div>
        <div>
          <img src="https://cdn.mos.cms.futurecdn.net/s5bepu6vYYSMJJDoYy2oXD-1200-80.jpg" alt="Flower 2" />
          <p className="legend">Sunflower</p>
        </div>
        <div>
          <img src="https://www.nature-and-garden.com/wp-content/uploads/sites/4/2022/04/lily-1320x989.jpg" alt="Flower 3" />
          <p className="legend">Lily</p>
        </div>
        <div>
          <img src="https://rukminim2.flixcart.com/image/850/1000/kit6hzk0-0/plant-seed/u/e/i/10-lotus-ss-online-original-imafygqmnr2xrjv4.jpeg?q=90&crop=false" alt="Flower 4" />
          <p className="legend">Lotus</p>
        </div>
        <div>
          <img src="https://hgic.clemson.edu/wp-content/uploads/2004/12/chinese-hibiscus-hibiscus-rosa-sinensis-has-four.jpeg" alt="Flower 5" />
          <p className="legend">Hibiscus</p>
        </div>
      </Carousel>
    </div>
  );
}

export default App;

