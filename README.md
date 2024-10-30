```markdown
# TikTok User Profile Scraper

This Python script uses Selenium to scrape user profile data from TikTok based on search terms provided by the user. The data includes usernames, followers count, likes count, bio text, and bio links. The scraped data is saved to a CSV file named `tiktok_profiles.csv`.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Code Overview](#code-overview)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before running this script, ensure you have the following installed:

- Python 3.x
- Chrome WebDriver (compatible with your version of Chrome)
- Required Python packages:
  - Selenium
  - pandas

You can install the necessary Python packages using pip:

```bash
pip install selenium pandas
```

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/ppreston21/tiktok-crawl.git
   cd tiktok-crawl
   ```

2. Download and place the Chrome WebDriver in a location accessible by your PATH or specify its location in the script.

## Usage

1. Open your terminal or command prompt.
2. Navigate to the directory where the script is located.
3. Run the script using Python:

   ```bash
   python start_3.py
   ```

4. When prompted, enter search terms separated by commas. For example:

   ```
   crypto trading, top g, excellent adventure, trump 2024, night at the museum
   ```

5. The script will open a Chrome window, perform searches on TikTok, and collect user profile data.

## Code Overview

- **WebDriver Initialization**: The script initializes a Chrome WebDriver to automate browser actions.
- **User Input**: It prompts the user to input search terms, which it splits into a list.
- **Searching TikTok**: For each search term, the script:
  - Navigates to TikTok's search page.
  - Enters the search term into the search bar.
  - Collects usernames from the search results.
- **Profile Data Collection**: For each username, it gathers:
  - Followers count
  - Likes count
  - Bio text
  - Bio link
- **Data Storage**: The collected data is appended to a CSV file named `tiktok_profiles.csv`.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### Adjustments Made:
- Updated the repository link to point to your GitHub repository: `https://github.com/ppreston21/tiktok-crawl.git`.
- The content is structured to provide a clear overview and guide for users. 

Feel free to customize any part further as needed!
