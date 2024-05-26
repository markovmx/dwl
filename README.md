# dwl

dwl is a Python script designed to download photos from vk.com social network either from community walls or from saved photos of a user.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/methhae/dwl.git
   ```

2. Navigate to the project directory:

   ```bash
   cd dwl
   ```

3. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Getting VK Access Token

To use the `dwl` script, you need to obtain an access token from VK (VKontakte). Follow these steps to create a VK application and obtain the access token:

1. **Create VK Application:**

   - Go to the [VK Developers](https://vk.com/dev) website and log in with your VK account credentials.
   - Navigate to the [My Apps](https://vk.com/apps?act=manage) section.
   - Click on the "Create App" button.

2. **Fill in Application Details and Authorize:**

   - Find aplication id.
   - Create request in your web-browser with next url-string
     https://oauth.vk.com/authorize
     ?client_id=YOUR_APP_ID
     &redirect_uri=YOUR_REDIRECT_URI
     &scope=PERMISSIONS_SCOPE
     &response_type=code

3. **Obtain Access Token:**

   - After request you will redirect to similar path, here you find your access token:
     https://oauth.vk.com/blank.html#access_token=YOUR_ACCESS_TOKEN_WILL_BE_HERE&expires_in=86400&user_id=816994330

4. **Set Up `.env` File:**

   - In the project directory, create a file named `.env` if it doesn't already exist.
   - Open the `.env` file in a text editor.
   - Add the following line, replacing `your_token` with the access token you obtained:
     ```
     VK_ACCESS_TOKEN=your_token
     ```

5. **Save and Run:**
   - Save the `.env` file.
   - Now you can run the `dwl` script using the instructions provided in the README.md file.

By following these steps, you'll have successfully obtained the VK access token required for using the `dwl` script.

## Usage

Ensure you have created a `.env` file in the project directory with your VK access token in the format `VK_ACCESS_TOKEN=your_token`.

Run the script with the following command:

### Options:

- `--community`: This option indicates that you want to run the script in community mode. In community mode, the script will download photos from a VK community (group) based on the specified group name.

- `--saved`: This option indicates that you want to run the script in saved mode. In saved mode, the script will download photos from the saved photos album of your VK account.

- `--group_name <name>`: This option is required when running the script in community mode (`--community`). It allows you to specify the name of the VK group from which you want to download photos. Replace `<name>` with the actual name of the VK group.

### Examples:

1. **Download photos from a community:**

   ```bash
   python dwl.py --community --group_name my_community
   ```

   This command will run the script in community mode and download photos from the VK community named `my_community`.

2. **Download saved photos from your VK account:**
   ```bash
   python dwl.py --saved
   ```
   This command will run the script in saved mode and download photos from the saved photos album of your VK account.
