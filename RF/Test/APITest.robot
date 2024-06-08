*** Settings ***
Resource  ../Configuration/ResourceMaps.robot

*** Test Cases ***

Sum of 4 and 6 is must Equal to 10
    Create Root    sum
    Add Integer To Root    sum    number1    4
    Add Integer To Root    sum    number2    6
    ${req_body}=  Get Root As Dict    sum
    ${response}=  Call Api    http://127.0.0.1:8000    ${req_body}    sum
    Log    ${response}
    ${value}=  Get Field From Response    ${response}    Total
    Should Be Equal        '${value}'    '10'  


Role of Huginn is must Equal to user
    Create Root    hrole
    Add String To Root    hrole    id    Huginn
    ${req_body}=  Get Root As Dict    hrole
    ${response}=  Call Api    http://127.0.0.1:8000    ${req_body}    user/role  
    Log    ${response}
    ${value}=  Get Field From Response    ${response}    role
    Should Be Equal        '${value}'    'User'  

Role of Thor is must Equal to god
    Create Root    Trole
    Add String To Root    Trole    id    Thor
    ${req_body}=  Get Root As Dict    Trole
    ${response}=  Call Api    http://127.0.0.1:8000    ${req_body}    user/role  method=GET
    Log    ${response}

