# dwl

Python script designed to download photos from vk.com social network either from community walls or from saved photos of a user.

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

### Note:
- Before running the script, ensure you have created a `.env` file in the project directory with your VK access token. The access token should be in the format `VK_ACCESS_TOKEN=your_token`.

