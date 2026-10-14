# 3D Structural and Petrophysical Characterization of the Hugin Reservoir

Python | Pandas | NumPy | SciPy | Matplotlib | LAS well-log data | 3D visualization

## Overview

A well-based subsurface characterization project using the Equinor Volve Data Village, focused on well 15/9-19 BT2 and the Hugin reservoir.

The project integrates structural interpretations, well-survey data, formation picks, interpreted petrophysical logs, crossplot analysis, and 3D visualization.

## Work Done

- QC and integration of Hugin Top/Base, fault, well-pick, survey, and LAS datasets
- Reconciled BT2 well trajectory with Hugin formation picks
- Characterized PHIF, VSH, KLOGH, and SW within the Hugin interval
- Analyzed petrophysical relationships using crossplots
- Built 2D structural context and a 3D Hugin structural visualization
- Documented data limitations and requirements for reservoir-scale modeling

## Key Findings

- Interpreted PHIF is centered around 20%, with relatively limited variability.
- VSH indicates generally low-to-moderate shale content with greater variability.
- KLOGH shows strong heterogeneity, ranging from very low values to >3,400 mD.
- Crossplots indicate that porosity alone does not explain the observed permeability variability.
- Interpreted SW is predominantly high within the investigated Hugin interval.

## Tools

Python, Pandas, NumPy, SciPy, Matplotlib, LAS well-log data, 3D visualization

## Dataset & Source

**Volve Data Village — Equinor ASA**

The project uses publicly released Volve subsurface data covering geological, geophysical, well, and reservoir information.

https://marketplace.databricks.com/details/5c3558ef-315c-44dd-baef-7062ac301f22/Equinor-ASA_Volve-Data-Village


## Repository Structure
- Geophysical_Interpretations/
- Well_logs_pr_WELL/
- Well_technical_data/
- src/
- plots/
- reports/
- docs/
- qc/

## Purpose

- Demonstrate a reproducible Python workflow for integrating heterogeneous subsurface datasets into a well-scale structural and petrophysical characterization suitable for further reservoir-scale analysis.
