import streamlit as st
from web3 import Web3
import numpy as np
from sklearn.ensemble import IsolationForest
import pandas as pd
import json

# Connect to Ethereum node
web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
web3.eth.default_account = web3.eth.accounts[0]

# Load the smart contract
contract_address = '0xd9145CCE52D386f254917e481eB44e9943F39138'
with open('ProductCertification_abi.json', 'r') as f:
    contract_abi = json.load(f)
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Load and train the AI model
historical_data = pd.read_csv('historical_data.csv')
features = historical_data[['feature1', 'feature2', 'feature3']]  # Ensure correct features are used
model = IsolationForest(contamination=0.1)
model.fit(features)

# Streamlit UI
st.title("🌿 Blaze: Blockchain-Enabled AI for Ethical Product Sourcing")

# Add Product Section
st.header("🔄 Add New Product")
st.write("Please provide the product details below:")

col1, col2 = st.columns(2)
with col1:
    product_name = st.text_input("Product Name")
    fair_trade_certified = st.checkbox("Fair Trade Certified")

with col2:
    sustainability_score = st.slider("Sustainability Score", 0, 100, 85)

if st.button("Add Product"):
    if product_name:
        try:
            tx_hash = contract.functions.addProduct(
                product_name, sustainability_score, fair_trade_certified
            ).transact()
            receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
            st.success(f"Product added successfully! Transaction hash: {tx_hash.hex()}")
        except Exception as e:
            st.error(f"Error adding product: {str(e)}")
    else:
        st.error("Product name is required.")

# Divider for better separation of sections
st.markdown("---")

# Verify Product Section
st.header("✅ Verify Product")
st.write("Enter the product ID and features for verification:")

col1, col2, col3 = st.columns(3)
with col1:
    product_id = st.number_input("Product ID", min_value=1, step=1)

with col2:
    feature1 = st.number_input("Feature 1", min_value=0)

with col3:
    feature2 = st.number_input("Feature 2", min_value=0)

feature3 = st.number_input("Feature 3", min_value=0)

if st.button("Verify Product"):
    new_data = np.array([[feature1, feature2, feature3]])
    is_anomaly = model.predict(new_data)

    if is_anomaly == -1:
        st.error("🚨 Anomaly detected: Product does not comply with ethical sourcing standards.")
    else:
        try:
            is_verified = contract.functions.verifyProduct(product_id).call()
            if is_verified:
                st.success("✅ Product verified: Complies with ethical sourcing standards.")
            else:
                st.error("❌ Product failed to comply with smart contract conditions.")
        except Exception as e:
            st.error(f"Error verifying product: {str(e)}. Please ensure the contract is deployed correctly and the chain is synced.")

# Footer
st.markdown("<br><hr><center>Powered by Blockchain and AI</center>", unsafe_allow_html=True)
st.markdown("<br><hr><center>Made by Tushar and Kuldeep for Project Blaze.</center>", unsafe_allow_html=True)