-- docker-compose exec -i oracle sqlplus C\#\#MYUSER/password@//localhost:1521/ORCLCDB

CREATE TABLE Customers (
    CustomerID INT,
    FirstName VARCHAR(100),
    LastName VARCHAR(100),
    DateOfBirth DATE,
    Address VARCHAR(255),
    Phone VARCHAR(50),
    Email VARCHAR(100)
);

CREATE TABLE Policies (
    PolicyID INT,
    CustomerID INT,
    PolicyType VARCHAR(50),
    StartDate DATE,
    EndDate DATE,
    Premium DECIMAL(10, 2)
    --,FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

CREATE TABLE Claims (
    ClaimID INT,
    PolicyID INT,
    DateOfClaim DATE,
    Amount DECIMAL(10, 2),
    Status VARCHAR(50)
    --,FOREIGN KEY (PolicyID) REFERENCES Policies(PolicyID)
);

CREATE MATERIALIZED VIEW CustomerPolicyClaimsMV AS
SELECT 
    c.CustomerID,
    c.FirstName,
    c.LastName,
    c.DateOfBirth,
    c.Address,
    c.Phone,
    c.Email,
    p.PolicyID,
    p.PolicyType,
    p.StartDate,
    p.EndDate,
    p.Premium,
    cl.ClaimID,
    cl.DateOfClaim,
    cl.Amount,
    cl.Status
FROM 
    Customers c
JOIN 
    Policies p ON c.CustomerID = p.CustomerID
LEFT JOIN 
    Claims cl ON p.PolicyID = cl.PolicyID;
