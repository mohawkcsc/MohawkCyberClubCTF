<!-- LOGO -->
<div align="center">
  <a href="https://github.com/mohawkcsc/MohawkCyberClubCTF"> <img src="images\logo.png" alt="Logo" width="320" height="80"></a>
  <h2> Mohawk Cyber Club CTF </h2>
  <p> Mohawk CTF Description </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#intro">Introduction</a></li>
    <li>
      <a href="#structure">Structure</a>
      <ul>
        <li><a href="#structure-repository">Repository Structure</a></li>
        <li><a href="#structure-folder">Challenge Folder Structure</a></li>
      </ul>
    </li>
    <li><a href="#start">Start Contribute</a></li>
    <li><a href="#level">Difficulty Level</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


<h2 id="intro"> Introduction </h2>
<p>This is the repository for challenges developed by Mohawk student for MohawkCTF or CyberClub. Challenges are distributed as per Category and then the chall name with the pre-defined folder structure for challenge folder as defined below.
Every Challenge should have an in-detailed step wise writeup which should be password protected with flag as it's password and should also have a give up file with hints or writeup with the password provided in discord server.</p>

<h2 id="structure"> Repository Structure </h2>

<h3 id ="structure-repository"> Repository Structure</h3>
<p>The structure of repository should be Category > Difficulty Level > Your Challenge folder.
<p>Kindly check with exec or admins on discord if you are not sure about the category for the chall, difficulty or if you think if a chall could fall in 2 categories.</p>

<h3 id ="structure-folder"> Challenge Folder Structure</h3>
<p>The Challenge Folder Name should match your CTF challenge name and can represent the challenge hint, associated information, or the library used in the challenge.</p>
<p>The Challenge folder should have two main folders and one optional folder:</p>

<ol>
  <li><b>Solve Folder:</b> This folder should include a writeup, a 'give up' file, and a solve script if applicable.</li>
    <ul>
      <li>Writeup: This file requires a password for access, and the password must match the CTF flag obtained after solving the challenge.</li>
    </ul>
  <li><b>Publish Folder:</b> This folder should contain all the files to be published during the CTF.</li>
  <li><b>Src Folder</b> (optional): You can include source code or any additional information related to the challenge in this folder.</li>
</ol>

<p>The challenge folder should also include a README.md file containing the following information:</p>
<ol>
  <li><b>Challenge Name:</b> The name of your CTF challenge.</li>
  <li><b>Author:</b>  Your name or preferred nickname.</li>
  <li><b>Category:</b> This can be one of the following: Binary Exploitation, Cryptography, Forensics, General Skills, OSINT, Reverse Engineering, Web Exploitation. If you're uncertain, you can discuss it with admins and execs.</li>
  <li><b>Challenge Description:</b> A brief description of your CTF challenge.</li>
  <li><b>Difficulty:</b> Refer to the difficulty levels <a href="#level">here</a>. If you're unsure, don't hesitate to discuss it with admins and execs.</li>
  <li><b>Flags format:</b> MohawkCTF{ANY_TEXT} </li>
  <li><b>Hint:</b> Provide a small hint for your challenge if you wish, or simply mark it as 'n/a.'</li>
  <li><b>Additional Info:</b> Include any extra details or requirements specified by the authors, admins, or execs.</li>
  <li><b>Attached files:</b> Include the SHA256 value of any files attached to ensure their integrity.</li>
</ol>

<p><b>Note:</b> The information.yml file is primarily intended for future reference, in case we decide to create a CTF event on <a href="https://ctfd.io/"></a>. So please fill it out as thoroughly as possible.</p>

<h2 id ="Start"> Start Contribute </h2>

<p>This project is designed for learning, inspiration, and creating your own CTF challenges. We greatly appreciate any contributions you make.</p>
<p>If you have suggestions to improve this project, please refer to the contact section.</p>
<p>To contribute:</p>

1. Fork the Project
2. Create your CTF Branch (`git branch {YourBranchName}`)
3. Add all the nessassery file to your folder (`git add -A`)
3. Commit your Changes (`git commit -m 'Adding my CTF chall'`)
4. Push to the Branch (`git push origin {YourBranchName}`)
5. Open a Pull Request

<h2 id="level"> Difficulty Level </h2> 

<p><b>Begineer (100)</b>: Challenges solvable with just one command.</p>
<p><b>Easy (200)</b>: Challenges requiring more than one command to solve.</p>
<p><b>Medium (300)</b>: Challenges needing multiple commands and some prior knowledge.</p>
<p><b>Hard (400)</b>: Challenges involving multiple commands, prior knowledge, and a bit of online research.</p>
<p><b>Insane (500)</b>: Extremely challenging tasks demanding multiple commands, extensive knowledge, thorough online research, and possibly even custom scripting.</p>

<p><b>Note:</b> It's important to note that this CTF is primarily designed for students, with the "hardcore" difficulty range being beginner to medium level to ensure an accessible and educational experience.</p>

<h2 id ="contact"> Contact </h2>

Mohawk Cyber Club Mail: [cyberclub@mohawkcollege.ca](mailto:cyberclub@mohawkcollege.ca)
