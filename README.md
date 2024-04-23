### README.md
#### Project Title: Fake Bar Finder
This script uses Selenium WebDriver to automate the process of identifying a fake bar in a virtual weighing puzzle hosted at "http://sdetchallenge.fetch.com/". The puzzle presents nine bars, one of which is fake (lighter than the other gold bars), and the task is to find the fake bar using a minimal number of weighings.
<img width="639" alt="Screenshot 2024-04-23 at 4 06 28 PM" src="https://github.com/NPriyaK/FetchChallenge/assets/102847203/bec83609-f78a-4060-a9aa-61cf4f00b48a">

  <img width="439" alt="Screenshot 2024-04-23 at 4 06 52 PM" src="https://github.com/NPriyaK/FetchChallenge/assets/102847203/0e1ccff2-8daa-475f-97d1-cdedf6ccad77">



#### Prerequisites
1. **Python:** Ensure Python is installed on your system.
2. **Selenium:** Install Selenium library using `pip install selenium`.
3. **ChromeDriver:** Download the appropriate version of ChromeDriver that matches your Google Chrome version and system architecture. Ensure it is placed in the specified path in the script or update the path accordingly.

#### Setup Instructions
1. Clone the repository or download the script.
2. Update the `chromedriver` path in the script if necessary.
3. Install


### Overview of the Algorithm used
The algorithm utilizes a divide and conquer strategy specifically tailored to identify a bar that is lighter than the rest. This method efficiently narrows down the potential candidates using a minimal number of weighings.

### Steps of the Algorithm

1. **Divide the Bars into Three Groups:** The algorithm splits the total number of bars into three nearly equal groups.

2. **Weigh Two Groups Against Each Other:** Two of the three groups are placed on a balance scale:
   - If one side is lighter, the fake bar is among the bars on that lighter side, since the fake bar weighs less.
   - If both sides are equal (this scenario won't typically happen since the fake bar is lighter and must be on one of the sides if included), the fake bar is in the third group that wasn't weighed.

3. **Recursive Narrowing Down:** The algorithm then focuses on the group that was determined to be lighter and repeats the process:
   - The suspected group is divided into three smaller groups, and two of these are weighed.
   - This process continues, reducing the group size each time until only one bar remains.

4. **Identify the Fake Bar:** The last remaining bar after these steps is identified as the fake bar because it's the only one left unverified against others.


### Output:
<img width="404" alt="Screenshot 2024-04-23 at 4 16 15 PM" src="https://github.com/NPriyaK/FetchChallenge/assets/102847203/bd4998e7-95a7-4b16-b709-58e87751e50d">

