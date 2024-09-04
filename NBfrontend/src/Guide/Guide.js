import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Button } from 'react-bootstrap';
import './Guide.css';
import { useNavigate } from 'react-router-dom';

function Guide() {
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
            <h2>Guide to Using NearBees</h2>
<p>Welcome to the NearBees Guide! This section provides detailed information to help you get the most out of our flower recognition system. Explore the following topics to learn more:</p>

<h3>1. Overview of NearBees</h3>
<p>Discover how NearBees works and what sets it apart from other flower identification tools. Learn about the technology behind the scenes and how it accurately identifies flowers from your photos.</p>

<h3>2. How to Use the App</h3>
<ul>
  <li><strong>Uploading Photos:</strong> Step-by-step instructions on how to upload photos to NearBees for analysis.</li>
  <li><strong>Understanding Results:</strong> Explanation of how to interpret the results provided by NearBees, including flower names, information, and related flowers.</li>
  <li><strong>Troubleshooting:</strong> Common issues you may encounter and how to resolve them.</li>
</ul>

<h3>3. Advanced Features</h3>
<ul>
  <li><strong>Multiple Photo Uploads:</strong> Learn how to upload multiple photos for improved identification accuracy.</li>
  <li><strong>Custom Queries:</strong> How to use custom queries to search for specific types of flowers or related information.</li>
  <li><strong>Integration with Other Tools:</strong> How NearBees can be integrated with other apps and tools for a seamless experience.</li>
</ul>

<h3>4. FAQs</h3>
<ul>
  <li><strong>Q1: What types of flowers can NearBees identify?</strong> A1: NearBees can identify a wide range of flowers, including common and exotic species. The accuracy may vary based on the quality of the photo and the flower's visibility.</li>
  <li><strong>Q2: How should I prepare my photos for the best results?</strong> A2: Ensure that the flower is well-lit, in focus, and occupies most of the frame. Avoid filters and capture the flower from different angles if possible.</li>
  <li><strong>Q3: Can I use NearBees offline?</strong> A3: NearBees requires an internet connection to analyze photos and provide identification results.</li>
  <li><strong>Q4: How do I contact support if I have issues?</strong> A4: If you encounter any problems or have questions not covered in the guide, please contact our support team via the "Contact Us" page or email support@nearbees.com.</li>
</ul> <button className="btn btn-primary btn-go-to" onClick={() => navigate('/')}>Back to Main Page</button>
</div>

            </div>
          </div>
        </div>
      
        </div>
      </div>
    
  );
}

export default Guide;


