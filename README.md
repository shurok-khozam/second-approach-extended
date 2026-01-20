# RL Countermeasures selection - Second Approach
******

## Introduction
5G represents the most recent and sophisticated generation of mobile
communications. It boasts features such as rapid response times, minimal latency,
and substantial bandwidth.
These networks are increasing sharply in size as well as in functionality,
especially with the growth of the Internet of Things, which gave rise to
numerous challenges. Nowadays attackers are developing diverse techniques to
exploit vulnerable gaps like insufficient traffic monitoring and access
controls through the network. It became mandatory to define appropriate
countermeasures in order to defend these networks against different attack types.
In this article, we are using Double Deep Q-Network (DDQN) which is a
reinforcement learning (RL) algorithm that aims to mitigate DDoS attacks in
SDN as it is the backbone of 5G networks since it enables network administrators
to centralize control and management of the network

******
## Modules
******
### - Mininet Network
A Mininet-based network topology with an exposed Flask API.

For more details, refer to the corresponding [README.md](network/README.md) file.

### - Reinforcement Learning
A whole simulation and training process that depends on the Network module.

For more details, refer to the corresponding [README.md](reinforcement/README.md) file.

### - Tools - Hosts Topology Generator
A python script to generate a JSON topology file for hosts.

For more details, refer to the corresponding [README.md](tools/hoststopo/README.md) file.

******
## Requirements
******
To be able to run the project, you should have:

- **Ubuntu 20.04 LTS**:
  - Running as a main system or inside a VM.
- **Python v3.8**:
  - Requirements at [requirements.txt](requirements.txt).
- **Mininet v2.2.2**:
  - From [Mininet official website](https://mininet.org/download/).
- **Apache Maven 3.6.3**.
- **Gradle v4.4.1**.
- **JDK v1.8**:
  - Tested with Openjdk V 1.8.0_422.
- **CICFlowMeter v4.0**:
  - From [CICFlowMeter Github Repository](https://github.com/CanadianInstituteForCybersecurity/CICFlowMeter).
- **MHDDoS v2.4.1**:
  - From [MHDDoS Github Repository](https://github.com/MatrixTM/MHDDoS).
- **TShark 3.2.3**:
  - Git v3.2.3 packaged as 3.2.3-1.
