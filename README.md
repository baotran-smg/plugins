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

The plugin includes Tableau Building, Dashboard Planning, Dashboard Design, and Workbook Engineering. The workflow is in `plugins/tableau-building/skills/tableau-building/SKILL.md`: plan, design, implement, verify, and hand off. Each new dashboard project uses `SQL Query/`, `Design/`, `Config/`, and `Backup/` under its agreed project folder; existing folders keep their names. The plugin does not bundle Tableau or BigQuery credentials/connectors; users need their own access to any data or applications they use.
