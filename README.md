# **Blockchain-Based Supply Chain Management**

A blockchain-based solution that leverages decentralized ledger technology and smart contracts to enhance transparency, traceability, and efficiency in supply chain operations.

---

## **Table of Contents**

1. [Introduction](#introduction)  
2. [Features](#features)  
3. [Setup and Installation](#setup-and-installation)  
4. [Usage](#usage)  
5. [Dataset](#dataset)  
6. [Project Workflow](#project-workflow)  
7. [Results](#results)  
8. [Future Enhancements](#future-enhancements)  
9. [Contributing](#contributing)  
10. [License](#license)  
11. [Author](#author)  

---

## **Introduction**

This project focuses on improving supply chain management by implementing a blockchain-based system. It utilizes **Ethereum smart contracts** to create an immutable ledger for tracking products, verifying authenticity, and automating processes like payments and quality checks, ensuring trust and transparency among stakeholders.

Demo Video:    https://www.youtube.com/watch?v=gexcpl12Zio
---

## **Features**

- 📦 **Product Tracking**: Records product movements from origin to consumer on the blockchain.  
- 🔒 **Secure Data Access**: Restricts sensitive data to authorized parties using cryptographic controls.  
- 🤖 **Smart Contract Automation**: Automates supply chain processes like payments and certifications.  
- 📊 **Visualization Dashboard**: Displays real-time transaction logs and product status timelines.  

---

## **Setup and Installation**

### **Prerequisites**

- Node.js (v16 or higher)  
- Libraries:
  - `web3.js`
  - `truffle`
  - `express` (for backend API, if applicable)
  - `react` (for frontend dashboard, if applicable)
  - `ganache-cli` (for local blockchain testing)
- MetaMask (browser extension for blockchain interaction)

### **Installation**

1. Clone the repository:

    ```bash
    git clone https://github.com/ryl-tushar04/BlockchainInSupplyChain.git
    cd BlockchainInSupplyChain
    ```

2. Create and activate a virtual environment (if using Python components):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install required libraries:

    ```bash
    npm install
    ```

4. Set up environment variables:

    ```bash
    cp .env.example .env
    ```

    Update `.env` with blockchain network details (e.g., Infura API key, wallet private key).

---

## **Usage**

### **Run the Blockchain Application**

1. **Start the local blockchain** (if using Ganache):

    ```bash
    ganache-cli
    ```

2. **Deploy smart contracts**:

    ```bash
    truffle migrate --network development
    ```

3. **Run the application**:

    ```bash
    npm start
    ```

4. **Access the dashboard**:

   Open `http://localhost:3000` in a browser with MetaMask installed to interact with the blockchain.

5. **Track products**:

   Use `track_product.js` to add or update product details and query transaction history via the dashboard.

---

## **Dataset**

The dataset consists of sample supply chain data, including product details (e.g., ID, origin, destination) and transaction logs. You can access the sample dataset in the repository:

🔗 **[Sample Dataset](https://github.com/ryl-tushar04/BlockchainInSupplyChain/tree/main/data)**

---

## **Project Workflow**

### **1. Data Collection & Preprocessing**

- Collect product and transaction data from supply chain stakeholders.  
- Format data as JSON for smart contract interactions.  

### **2. Feature Engineering**

- Define product attributes (e.g., ID, timestamp, status).  
- Create transaction logs for blockchain storage.

### **3. Smart Contract Architecture**

- Solidity contracts for product tracking and access control.  
- Event-based logging for supply chain updates.

### **4. Deployment**

- Deploy contracts on a local or testnet blockchain.  
- Integrate with Web3.js for frontend/backend interaction.

---

## **Results**

### **System Performance**

| Metric                 | Value  |
|------------------------|--------|
| Transaction Throughput | 50 tx/s (local blockchain) |
| Latency (avg)          | 2s     |
| Data Integrity         | 100%   |
| Access Control         | 100% secure |

### **Visualization**

![Screenshot 2024-10-09 232614](https://github.com/user-attachments/assets/34be8eb1-a9d6-4fc4-85ac-0c8da4071dfd)

![image](https://github.com/user-attachments/assets/6e6e468e-5e6b-4523-a43b-e8964eb29e80)


---

## **Future Enhancements**

- Integrate IoT devices for real-time product tracking (e.g., location, temperature).  
- Support multiple blockchain platforms (e.g., Hyperledger, Polygon).  
- Add predictive analytics for supply chain optimization.  
- Deploy on cloud platforms for enterprise scalability.  

---

## **Contributing**

Contributions are welcome! Please follow these steps:

1. Fork the repository:

    ```bash
    git clone https://github.com/ryl-tushar04/BlockchainInSupplyChain.git
    ```

2. Create a new branch:

    ```bash
    git checkout -b feature-branch
    ```

3. Commit your changes:

    ```bash
    git commit -m "Add your message here"
    ```

4. Push to the branch:

    ```bash
    git push origin feature-branch
    ```

5. Create a pull request.

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Author**

**Tushar Saxena**  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/tushar-saxena0410/)

