// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ProductCertification {
    struct Product {
        string name;
        uint256 sustainabilityScore;
        bool fairTradeCertified;
    }

    mapping(uint256 => Product) public products;
    uint256 public productCount = 0;

    function addProduct(
        string memory name,
        uint256 sustainabilityScore,
        bool fairTradeCertified
    ) public returns (uint256) {
        productCount++;
        products[productCount] = Product(
            name,
            sustainabilityScore,
            fairTradeCertified
        );
        return productCount;
    }

    function verifyProduct(uint256 productId)
        public
        view
        returns (bool)
    {
        Product memory product = products[productId];
        if (
            product.sustainabilityScore >= 80 &&
            product.fairTradeCertified
        ) {
            return true;
        }
        return false;
    }
}
