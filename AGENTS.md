# AGENTS

## Development methodology

This repository is structured as a spec-driven, dark-factory workflow. All
system behavior, configuration, and code is defined via the specifications in
the `features` directory.

### Authoritative artifacts

The following artifacts are considered to be source-of-truth, defining the
specification of the system:

- [`/Vision.md`](Vision.md) - The high-level "vision" for the system/project,
  including its goals and objectives. Start here to understand the purpose of
  the system.
- [`/Architecture.md`](Architecture.md) - The architecture of the system,
  including its components and their interactions. This document provides a
  high-level overview of how the system is structured. It should not contain
  implementation details, only the high-level components and their interfaces
  to each other and the external world
- [`/features/**`](features) - This directory contains the specifications for
  the system's features, written in Gherkin syntax. Each feature is an EARS
  (Easy Approach to Requirements Syntax) rule, which describes a specific
  behavior or functionality of the system. The scenarios within each feature
  file ensure the system accurately implements the specified behavior.
- [`/AGENTS.md`](AGENTS.md) and [`/.agents/**`](.agents) - These files contain
  the definitions of the agents that are used to develop and test the system.

All other artifacts in the repository are considered to be derived from these
authoritative artifacts. It should be possible to delete any other artifact
and regenerate it from the authoritative artifacts.

### Development workflow

The development workflow is as follows:

- When the user wants to add a new feature, fix a bug, or make any other
  change to the system, you should use the `eliciting-requirements` skill to
  interactively work with the user to create the EARS rules that define the
  desired behavior. This process should be done in a conversational manner,
  with the user providing input and feedback as needed.
- These EARS rules should be added as feature files in the `features`
  directory (one rule per file). Name the feature files based on a slugified
  version of the EARS rule.
- Create scenarios within each feature file to ensure that the system
  accurately implements the specified behavior. Use property-based testing
  where possible to generate a wide range of test cases and ensure that the
  system behaves correctly in all situations.
- Implement the system behavior defined in the feature files. This may involve
  writing code, configuring the system, or making other changes as needed.
- Implement the steps defined in the feature files so that the tests are
  executable.
