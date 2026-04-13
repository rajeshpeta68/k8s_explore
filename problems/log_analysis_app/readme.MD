🧩 Real-Time Requirement: “Log Processing & Analytics Platform”
🎯 Problem Statement

Your company runs multiple applications and needs:

Centralized log collection
Real-time log processing API
A UI dashboard to view logs in browser
Secure and scalable architecture
Controlled access between components

===============================================

Users (Browser)
     ↓
Ingress (logs.local)
     ↓
Frontend (Dashboard UI)
     ↓
Log API Service
     ↓
Elasticsearch (Stateful storage)

+ Fluentd (DaemonSet) → Collect logs from all nodes
+ CronJob → Cleanup old logs
+ HPA → Scale API under load
+ NetworkPolicy → Restrict Elasticsearch
+ ConfigMaps/Secrets → Config + credentials

======================================