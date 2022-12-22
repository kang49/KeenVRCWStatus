<h1>Keen_status Document</h1>
<p>Welcome to the VRChat Heart Rate Status Updater!</p>
<p>This program is designed to log into your VRChat account, navigate to your profile page, and update your status with a constantly fluctuating heart rate. </p>
<h2>Prerequisites</h2>
<p>Before you can use this program, you will need to have the following installed:</p>
<ul>
  <li>Python 3.7 or later</li>
  <li>The selenium library</li>
  <li>The colorama library</li>
  <li>A webdriver (such as ChromeDriver)</li>
</ul>
<h2>Setup</h2>
<p>To set up the program, follow these steps:</p>
<ol>
  <li>Clone or download the repository to your local machine.</li>
  <li>Open the <code>keen_status.py</code> file in a text editor.</li>
  <li>Replace the <code>username</code> variable with your VRChat username. Don't forget to change this info to your username!</li>
  <li>In the command line, navigate to the directory where the program is located.</li>
  <li>Run the program with the command <code>python keen_status.py</code>.</li>
</ol>
<h2>Usage</h2>
<p>When you run the program, it will prompt you for your VRChat password. Enter your password and press enter. If you have enabled two-factor authentication for your account, the program will also prompt you for your two-factor code. </p>
<p>The program will then open a web browser window (if the headless option is set to False) and log into your VRChat account. It will navigate to your profile page and begin updating your status with a fluctuating heart rate. The heart rate will start at a rate of 68 beats per minute and fluctuate by a random amount between -3 and 3 every iteration of the loop. The total fluctuation is tracked and if it exceeds 10 within a 30-minute period, it is reset to 0. If the heart rate goes above 80, it is gradually decreased by 1. The program will continue to update your status until you stop it by pressing <code>CTRL + C</code> in the command line.</p>
<h2>Customization</h2>
<p>You can customize the program by modifying the following variables:</p>
<ul>
  <li><code>current_rate</code>: This variable determines the starting heart rate for the program.</li>
  <li><code>headless</code>: This variable determines whether the program will run in the background or with a visible browser window. Set to <code>True</code> for a headless program and <code>False</code> for a program with a visible window.</li>
</ul>
<h2>Troubleshooting</h2>
<p>If you encounter any issues while using the program, try the following solutions:</p>
<ul>
    <li>Make sure you have the required libraries and webdriver installed.</li>
    <li>Make sure you have entered the correct VRChat username and password.</li>
    <li>If the program is not updating your status, try increasing the sleep time between status updates.</li>
    <li>If the program is running slowly, try decreasing the sleep time between status updates or setting the headless option to <code>True</code>.</li>
</ul>
<p>We hope you enjoy using the VRChat Heart Rate Status Updater!</p>