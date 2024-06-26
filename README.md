<p align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/6295/6295417.png" width="100" />
</p>
<p align="center">
    <h1 align="center">CNCZEROTIER</h1>
</p>
<p align="center">
    <em>This repository implements a simple Command and Control (CnC) system using ZeroTier, a virtual networking service that allows devices to connect securely over the internet. The CnC system is divided into a client and server structure, facilitating remote management and communication between devices.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/RaditPasya/CnCZeroTier?style=flat&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/RaditPasya/CnCZeroTier?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/RaditPasya/CnCZeroTier?style=flat&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/RaditPasya/CnCZeroTier?style=flat&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
</p>
<hr>

##  Quick Links

> - [ Overview](#-overview)
> - [ Repository Structure](#-repository-structure)
> - [ Modules](#-modules)
> - [ Getting Started](#-getting-started)
>   - [ Installation](#-installation)
>   - [ Running CnCZeroTier](#-running-CnCZeroTier)
> - [ License](#-license)

---

##  Overview

The CnCZeroTier project facilitates a secure and efficient Command and Control system using ZeroTier for network connectivity. The client-server architecture allows for remote management and execution of tasks, making use of Python for both client and server implementations. The repository includes all necessary scripts and dependencies to set up and run the CnC system.
---


##  Repository Structure

```sh
└── CnCZeroTier/
    ├── Client
    │   ├── main.py
    │   ├── randomizer.py
    │   ├── scan_wifi.py
    │   ├── socket_client.py
    │   └── test.py
    ├── README.md
    ├── Server
    │   ├── client_handler.py
    │   ├── server.py
    │   ├── server_actions.py
    │   └── shared_data.py
    └── requirements.txt
```

---

## Modules

<details closed><summary>.</summary>

| File                                                                                       | Summary                                                                                               |
| ---                                                                                        | ----------------------------------------------------------------------------------------------------- |
| [requirements.txt](https://github.com/RaditPasya/CnCZeroTier/blob/master/requirements.txt) | Lists the Python dependencies required to run the project, such as `zerotier`, `socket`, and `pytest` |

</details>

<details closed><summary>Server</summary>

| File                                                                                                | Summary                                                                                             |
| ---                                                                                                 | --------------------------------------------------------------------------------------------------- |
| [client_handler.py](https://github.com/RaditPasya/CnCZeroTier/blob/master/Server/client_handler.py) | Manages incoming client connections, handling their communication and interaction with the server.  |
| [shared_data.py](https://github.com/RaditPasya/CnCZeroTier/blob/master/Server/shared_data.py)       | Maintains shared data structures and variables for use by the server and clients.                   |
| [server.py](https://github.com/RaditPasya/CnCZeroTier/blob/master/Server/server.py)                 | The main server script, responsible for initializing the server and managing its operations.        |
| [server_actions.py](https://github.com/RaditPasya/CnCZeroTier/blob/master/Server/server_actions.py) | Defines the actions and commands that the server can execute in response to client requests.        |

</details>

<details closed><summary>Client</summary>

| File                                                                                              | Summary                                                                                             |
| ---                                                                                               | --------------------------------------------------------------------------------------------------- |
| [main.py](https://github.com/RaditPasya/CnCZeroTier/blob/master/Client/main.py)                   | The main client script, initializing and managing the client-side operations.                       |
| [randomizer.py](https://github.com/RaditPasya/CnCZeroTier/blob/master/Client/randomizer.py)       | Contains functions for generating random data, possibly for obfuscation or testing purposes.        |
| [socket_client.py](https://github.com/RaditPasya/CnCZeroTier/blob/master/Client/socket_client.py) | Manages the client-side socket connections to the server, handling communication protocols.         |
| [scan_wifi.py](https://github.com/RaditPasya/CnCZeroTier/blob/master/Client/scan_wifi.py)         | Implements functionality to scan available Wi-Fi networks.                                          |
| [test.py](https://github.com/RaditPasya/CnCZeroTier/blob/master/Client/test.py)                   | Includes test cases for validating the functionality of the client-side code.                       |

</details>


##  Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **Python**: `version x.y.z`

### Installation

1. Clone the CnCZeroTier repository:

```sh
git clone https://github.com/RaditPasya/CnCZeroTier
```

2. Change to the project directory:

```sh
cd CnCZeroTier
```

3. Install the dependencies:

```sh
pip install -r requirements.txt
```

### Running CnCZeroTier

1. Ensure ZeroTier is running and all clients are on the same network.

2. To run the server, go to the server folder and run `server.py`:

```sh
cd Server
python server.py
```

3. To run the client, go to the client folder and run `main.py`:

```sh
cd Client
python main.py
```


---



##  License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments


[**Return**](#-quick-links)

---