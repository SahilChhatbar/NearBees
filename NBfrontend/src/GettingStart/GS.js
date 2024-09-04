import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './GS.css';
import { useNavigate } from 'react-router-dom';

function GS() {
  const navigate = useNavigate();

  return (
    <div className="App">
      
      <MainContent navigate={navigate} />
    </div>
  );
}

function Header() {
  return (
    <header className="App-header">
      <img className="logo" src="NearBees.png" alt='NearBees' />
    </header>
  );
}

function MainContent({ navigate }) {
  return (
    <div className="container mt-4">
      <div className="overlay"></div>
      <div className="overlay-content">
        <div className="row">
          <div className="col-md-12">
            <div className="page">
              <div className='a'>
                <h2>Getting Started with NearBees</h2>
                <p>Welcome to NearBees! Follow these simple steps to start identifying flowers:</p>
                <h4>Step 1: Capture the Flower</h4>
                <p>Use your smartphone or camera to take a clear, close-up photo of the flower you want to identify. Ensure the image is well-lit and the flower is centered in the frame for the best results.</p>
                <h4>Step 2: Upload the Photo</h4>
                <p>Click on the "Upload Photo" button on the main page. Select the photo you just captured from your device. NearBees will analyze the image to identify the flower.</p>
                <h4>Step 3: View Your Results</h4>
                <p>Once the analysis is complete, NearBees will display the name of the flower along with additional information about it. You can also explore related flowers and learn more about their characteristics.</p>

                <h3>Tips for Best Results</h3>
                <ul>
                  <li><strong>Focus on the Flower:</strong> Ensure that the flower is in focus and occupies most of the frame. Avoid capturing too much background, as it may interfere with the identification process.</li>
                  <li><strong>Good Lighting:</strong> Natural lighting works best. If indoors, try to avoid shadows and use soft light to illuminate the flower.</li>
                  <li><strong>Multiple Angles:</strong> If possible, take photos from different angles and upload them one at a time to get the most accurate identification.</li>
                  <li><strong>Avoid Filters:</strong> Upload the original photo without any filters or edits to ensure the system can accurately analyze the flower's features.</li>
                </ul>
                <button className="btn btn-primary btn-go-to" onClick={() => navigate('/')}>Back to Main Page</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default GS;
