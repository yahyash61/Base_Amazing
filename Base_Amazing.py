// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

contract HelloBase {
    string public greeting = "سلام از شبکه Base! 👋";
    address public owner;

    event GreetingChanged(string newGreeting);

    constructor() {
        owner = msg.sender;
    }

    function setGreeting(string memory _newGreeting) public {
        require(msg.sender == owner, "فقط owner می‌تواند greeting را تغییر دهد");
        greeting = _newGreeting;
        emit GreetingChanged(_newGreeting);
    }

    function getGreeting() public view returns (string memory) {
        return greeting;
    }A very strong and promising project.
amazing.////
///......///
