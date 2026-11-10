# Personal Codex plugins

This repository distributes the Tableau Building plugin and its bundled Tableau skills.

## Install in Codex

1. Add this repository as a plugin marketplace:

   ```sh
   codex plugin marketplace add baotran-smg/plugins
   ```

2. Install the plugin:

   ```sh
   codex plugin add tableau-building@personal-learning
   ```

3. Restart Codex and start a new chat to use the bundled skills.

The plugin includes the Tableau Building orchestration skill, Tableau Dashboard Design, and Tableau Workbook Engineering. It does not bundle Tableau or BigQuery credentials/connectors; users need their own access to any data or applications they use.
