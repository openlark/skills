---
name: loop-engineering
description: Loop Engineering AI Programming Paradigm Guide. Explains the core concepts of transitioning from single Prompt calls to autonomous loop systems, key components (Automations/Worktrees/Skills/Plugins/Sub-agents), /loop and /goal primitives, and differences from Prompt Engineering and Harness Engineering. 
---

# Loop Engineering

Loop Engineering is a new paradigm for AI programming. By designing autonomous loop systems, agents can continuously execute tasks in an environment with goals, feedback, and self-verification — no longer dependent on manual prompts.

## Use Cases

Use when users need to understand "Loop Engineering", "AI Loop Systems", "Autonomous Agent Design", "/loop", "/goal", "AI Programming Paradigms", "System Architecture".

## Core Concept

Shift from single Prompt calls to persistent loop systems:

| Paradigm | Workflow | Developer Role |
|----------|----------|----------------|
| Prompt Engineering | Manually input prompts, model executes once, human judges result | Prompt Engineer |
| Harness Engineering | Build a constrained environment for a single agent with pre-checks/fixes/hooks, still requires human triggers | Harness Engineer |
| Loop Engineering | Orchestrate multi-agent timing, decisions, and autonomous loops — long-running multi-round automatic progression | System Architect / Loop Engineer |

## Key Components

### 1. Automations
- Trigger task discovery and processing on a schedule or by events
- Support periodic runs and archival mechanisms

### 2. Worktrees
- Manage task state and context
- Enable agents to maintain memory and state persistence across multiple loops

### 3. Skills
- Encapsulate reusable sub-tasks as skills
- Callable by the loop system

### 4. Plugins / Connectors
- Extend system capabilities
- Interact with external tools or services

### 5. Sub-agents
- Small agents for division of labor
- Support parallel multi-agent task execution

### 6. External Memory & Feedback Loop
- Through logs, test results, type checking, and other mechanisms
- Agents self-evaluate and self-correct, avoiding meaningless loops

## /loop and /goal Primitives

| Primitive | Behavior | Use Case |
|-----------|----------|----------|
| `/loop` | Execute tasks repeatedly on a cycle | Scheduled checks, periodic maintenance |
| `/goal` | Run continuously until verifiable conditions are met | Goal-oriented autonomous tasks, each round checked by an independent model |

## Design Principles

When designing a Loop Engineering system, focus on:

- **Goal Definition**: Clearly define verifiable completion conditions to prevent agents from falling into meaningless loops
- **Feedback Mechanism**: Enable agent self-evaluation through tests, validation, logs, etc.
- **State Management**: Use Worktrees to maintain cross-round context and memory
- **Modularity**: Encapsulate reusable capabilities as Skills and Plugins
- **Division of Labor**: Properly assign Sub-agent responsibilities, improve efficiency through parallelism
- **Graceful Termination**: Set timeouts, maximum rounds, and abnormal exit conditions