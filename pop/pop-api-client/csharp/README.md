# VeriBlock PoP Miner API Client
This sample demonstrates how a custom application might utilize the embedded HTTP API in a PoP miner to automate certain decisions. In doing so, the sample will demonstrate several of the API's available. For a complete list of available endpoints in the embedded API, please see this reference documentation:

* https://wiki.veriblock.org/index.php?title=PoP_Miner_API

## Overview
Proof-of-proof mining is a competitive endeavor to have your endorsement of the state of a blockchain (VeriBlock) included in the earliest possible block in a security-providing blockchain (Bitcoin). 

In this sample, we will build a console application to configure and control behavior of the PoP miner. First, the miner will be configured to auto-mine only rounds 2 & 4, using a specific BTC transaction fee per KB. A discussion of VeriBlock rounds can be found at:

* https://wiki.veriblock.org/index.php?title=HowTo_run_PoP_Miner#VeriBlock_.22Rounds.22

The application will then execute a task on a 10-minute interval. At each execution of the task, the following logic will execute:

1. Use the "GET /api/operations" endpoint to retrieve the current running operations and count up the number that are waiting for a BTC transaction to be included in a block
2. If the number of pending transactions is greater than some threshold:
   1. Use the "PUT /api/configuration" endpoint to turn off auto-mining on round 2 blocks
   2. Use the "PUT /api/configuration" endpoint to raise the configured transaction fee per kb
   3. Use the "POST /api/mine" endpoint to submit a new mining operation at the higher fee
   4. Use the "PUT /api/configuration" endpoint to reset the configured transaction fee per kb to the original value
3. If the number of pending transactions is greater than some higher threshold:
   1. Use the "PUT /api/configuration" endpoint to turn off auto-mining on all rounds
4. If the number of pending transactions returns to an "acceptable" level and any pausing of auto-mine had been taken previously:
   1. Use the "PUT /api/configuration" endpoint to turn on auto-mining for rounds 2 & 4

_DISCLAIMER: Please note that the strategy outlined in this sample is solely designed to demonstrate how one might compose available API endpoints into a decision-making algorithm. The strategy itself and all amounts, values or thresholds should not be considered guidance or recommendation._