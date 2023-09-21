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
This repository contains challenges developed by a student from Mohawk for use in MohawkCTF or CyberClub. Challenges are categorized by type, further sorted by difficulty level, and finally organized into individual challenge folders, following the predefined folder structure as detailed below.

Each challenge must include a comprehensive step-by-step writeup, which should be password-protected using the flag as the password. Additionally, a README.md file should be present in each challenge folder, providing the challenge's name and essential information."

<li>Flag Format: MohawkCTF{ANY_TEXT}</li>

<h2 id="structure"> Repository Structure </h2>

<h3 id ="structure-repository"> Repository Structure</h3>
<p>The structure of repository should be Category > Difficulty Level > Your Challenge folder.
<p>If you're uncertain about the challenge's category, difficulty level, or if it could belong to multiple categories, please consult with the executives or administrators on Discord for clarification.</p>

<h3 id ="structure-folder"> Challenge Folder Structure</h3>
<p>The name of the Challenge Folder should correspond to your CTF challenge name. CTF challenge name can be relevant challenge hints, associated information, or the library used in the challenge.</p>
<p>The Challenge folder structure should consist of two primary directories, with an optional third directory: </p>

<ol>
  <li><b>Solve Folder:</b> This directory should house a writeup file, and optionally, a solve script if applicable.</li>
    <ul>
      <li>Writeup: Access to this file requires a password that matches the CTF flag obtained after successfully solving the challenge.</li>
    </ul>
  <li><b>Publish Folder:</b> This directory should contain all the files intended for publication.</li>
  <li><b>Src Folder</b> (optional): Inclusion of source code or any supplementary materials relevant to the challenge can be placed within this folder.</li>
</ol>

The challenge folder should also include a README.md file containing the following information:

1. **Challenge Name:** The name of your CTF challenge.
2. **Author:**  Your name or preferred nickname.
3. **Category:** This can be one of the following: Binary Exploitation, Cryptography, Forensics, General Skills, OSINT, Reverse Engineering, Web Exploitation. If you're uncertain, you can discuss it with admins and execs.
4. **Challenge Description:** A brief description of your CTF challenge.
5. **Difficulty:** Refer to the difficulty levels <a href="#level">here</a>. If you're unsure, don't hesitate to discuss it with admins and execs.
6. **Flags format:** `MohawkCTF{ANY_TEXT}`
7. **Hint:** Provide a small hint for your challenge if you wish, or simply mark it as 'n/a.'
8. **Additional Info:** Include any extra details or requirements specified by the authors, admins, or execs.
9. **Attached files:** Include the SHA256 value of any files attached to ensure their integrity.

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
