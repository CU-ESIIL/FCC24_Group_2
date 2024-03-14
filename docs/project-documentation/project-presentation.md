# Project presentation overview

All project presentation materials should be made available on this page. Your team may present directly from this page if you would like to; alternatively, if you would prefer to use slides to present, please make sure to export your team's slides as a PDF, add them to your GitHub, and add the link to that PDF here below.

# Presentation

## Introduction:
Satellite remote sensing has revolutionized our understanding of the Earth's surface by providing vast amounts of data covering large spatial extents. However, each remote sensing dataset comes with its own strengths and limitations. GLAD ARD offers comprehensive coverage with frequent revisit times, making it ideal for monitoring land cover changes over time. On the other hand, GEDI LiDAR data provides high-resolution measurements of forest structure and biomass, enabling detailed analyses at a finer scale. Integrating these datasets offers a promising solution to enhance our understanding of ecosystem dynamics and support various environmental management applications.

## Objectives:
Develop machine learning models (e.g., gradient boosted regression, Light GBM, XGBoost) to predict GEDI LiDAR metrics based on GLAD ARD spectral features.
Explore techniques for harmonizing and scaling the two datasets to facilitate seamless integration.
Evaluate the performance of the integrated model in producing wall-to-wall maps of forest structure, biomass, and land cover.
Assess the spatial and temporal variations captured by the integrated dataset and compare them with ground-truth measurements and existing products.

# Methodology:
## Data Preprocessing: 
Clean and preprocess GLAD ARD and GEDI LiDAR datasets, including outlier removal, normalization, and feature selection.
Model Training: Implement machine learning algorithms to train predictive models using GLAD ARD spectral features as input and GEDI LiDAR metrics as target variables.
Model Evaluation: Validate the performance of trained models using cross-validation techniques and appropriate evaluation metrics (e.g., RMSE, R-squared).
Integration: Develop algorithms to integrate predictions from GLAD ARD and GEDI LiDAR models, considering spatial and temporal variations.
Wall-to-Wall Mapping: Generate wall-to-wall maps of forest structure, biomass, and land cover using the integrated dataset and assess their accuracy and reliability.

## Expected Outcomes:
A robust machine learning framework for integrating GLAD ARD and GEDI LiDAR data.
Wall-to-wall maps providing comprehensive insights into forest structure, biomass, and land cover dynamics at various scales.
Improved understanding of ecosystem dynamics and environmental changes, facilitating informed decision-making for sustainable land management and conservation efforts.

## Significance:
The integrated dataset produced by this project will have significant implications for various applications, including carbon accounting, biodiversity monitoring, and natural resource management. By leveraging the complementary strengths of GLAD ARD and GEDI LiDAR data, our approach will contribute to advancing global-scale monitoring efforts and supporting evidence-based policy decisions aimed at mitigating the impacts of climate change and promoting ecosystem resilience.

## Conclusion:
Our project represents a novel approach to integrating multi-resolution remote sensing datasets for comprehensive land cover mapping and monitoring. By combining machine learning techniques with state-of-the-art data harmonization methods, we aim to create a valuable resource for researchers, policymakers, and conservation practitioners seeking to understand and manage terrestrial ecosystems in a rapidly changing world.

### References:

[GLAD](https://glad.umd.edu/ard/home) dataset:
Potapov, P., Hansen, M.C., Kommareddy, I., Kommareddy, A., Turubanova, S., Pickens, A., Adusei, B., Tyukavina A., and Ying, Q., 2020. Landsat analysis ready data for global land cover and land cover change mapping. Remote Sens. 2020, 12, 426; doi:10.3390/rs12030426

[Link](https://de.cyverse.org/data/ds/iplant/home/shared/earthlab/forest_carbon_codefest/Team_outputs/Team2?selectedOrder=asc&selectedOrderBy=name&selectedPage=0&selectedRowsPerPage=100) to our datastore.
