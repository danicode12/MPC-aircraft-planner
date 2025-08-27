# MPC-Based Aircraft Trajectory Planner

This project implements a **Model Predictive Control (MPC)**-based aircraft trajectory planner with realistic aviation constraints.  
It will evolve in phases, starting from simple vertical climb control and extending to full trajectory planning with wind forecasts.

## 🚀 Project Roadmap (hopefully and ideally) - Check them off as you go

- **Phase 1 – Vertical Climb MPC**  
  Model altitude & vertical speed (`h, ḣ`), input is vertical acceleration.  
  Task: climb from 10,000 → 30,000 ft smoothly, subject to climb rate limits.

- **Phase 2 – Lateral Waypoint Tracking**  
  2D kinematic aircraft model (`x, y, ψ`) with constant speed.  
  Input: bank angle → turn rate. Task: follow waypoints smoothly with bank ≤ 30°.

- **Phase 3 – Rolling Horizon (Real-Time MPC)**  
  Solve MPC at each step, apply first input, re-plan under disturbances (crosswind).

- **Phase 4 – Integration with Prediction**  
  Add simulated wind forecasts and show how prediction improves planning.

- **Phase 5 – Packaging**  
  Visualization (matplotlib/folium), polished repo, demo video.

## 📂 Repo Structure

