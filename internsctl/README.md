# Internsctl

Internsctl is a versatile command-line utility designed to manage system resources and user accounts on a Linux server. It simplifies tasks such as retrieving CPU and memory information, managing file attributes, and handling user accounts.

## Features

- Retrieve detailed CPU information.
- Display memory usage in a human-readable format.
- Manage file attributes such as size, permissions, owner, and last modification time.
- Create new user accounts and list existing ones, including those with sudo privileges.

## Installation

To install internsctl, clone the repository or download the script directly. Then, make the script executable:

```bash
chmod +x internsctl
```

Optionally, you can move the script to a directory in your PATH for easier access.

### Installing the Man Page

To install the man page for internsctl, copy the `internsctl.1` file to your man pages directory (typically `/usr/share/man/man1/`) and update the man database. This might require superuser privileges:

```bash
sudo cp internsctl.1 /usr/share/man/man1/
sudo mandb
```

## Usage

The `internsctl` script can be used with the following commands:

- **CPU Information**:
  ```
  internsctl cpu getinfo
  ```

- **Memory Information**:
  ```
  internsctl memory getinfo
  ```

- **File Information**:
  - All Information: `internsctl file getinfo <file>`
  - Size: `internsctl file getinfo --size <file>`
  - Permissions: `internsctl file getinfo --permissions <file>`
  - Owner: `internsctl file getinfo --owner <file>`
  - Last Modified: `internsctl file getinfo --last-modified <file>`

- **User Management**:
  - Create User: `internsctl user create <username>`
  - List Users: `internsctl user list`
  - List Users with Sudo: `internsctl user list --sudo-only`

## Documentation

For complete documentation, refer to the manual page:

```bash
man internsctl
```

## Contributing

Contributions to internsctl are welcome! Please fork the repository, make your changes, and submit a pull request.

## Authors

- Kashish Koushal - 20bce104@nith.ac.in

## Acknowledgments

- Thanks to everyone who has contributed to the development of this utility.

