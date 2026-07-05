# Self-Driving Cars: Complete Roadmap, Resources & Career Guide

*Built for a BSCS student with a Computer Vision + ML/AI background, aiming to move into autonomous vehicles.*

---

## How This Roadmap Is Structured

Self-driving is not one field — it's five fields stacked on top of each other:

```
Perception (see the world) 
    → Localization (know where you are)
        → Prediction (guess what others will do)
            → Planning (decide what to do)
                → Control (execute it on the vehicle)
```

You already have a head start on **Perception** (CV641, SIFT, convolution, NAVTTC ML). The roadmap below is ordered so each phase unlocks the next.

---

## PHASE 0 — Math Refresher (parallel, ongoing)

You don't need to "finish" math before starting — but you need enough to not get stuck later. Treat this as a background track you top up as needed.

| Topic | Why it matters | Resource |
|---|---|---|
| Linear Algebra | Transforms between camera/LiDAR/world frames, NN internals | *3Blue1Brown - Essence of Linear Algebra* (YouTube, free), MIT 18.06 (Gilbert Strang, OCW, free) |
| Probability & Statistics | Kalman filters, Bayesian inference, sensor noise | Khan Academy Probability, *Think Bayes* (free book) |
| Multivariable Calculus | Backprop, gradients, Jacobians | MIT 18.02 OCW |
| Control Theory basics | PID, state-space, MPC | *Brian Douglas - Control Systems Lectures* (YouTube, free) |
| Optimization | Gradient descent variants, convex opt | Stephen Boyd's *Convex Optimization* (Stanford, free PDF + lectures) |

**Don't binge all of this upfront.** Pull each topic in when a project forces you to need it — that's when it sticks.

---

## PHASE 1 — Solidify ML/DL Foundations (1–2 months)

You have KNN/DT/RF from your career-advisor project. Now go deep learning.

- **Course:** Andrew Ng's *Machine Learning Specialization* (Coursera, DeepLearning.AI) — if not done already
- **Course:** *Deep Learning Specialization* (DeepLearning.AI, Coursera) — covers CNNs, sequence models
- **Book:** *Dive Into Deep Learning* (d2l.ai) — free, code-first, pairs well with your CLI/Fedora workflow
- **Practice:** Kaggle competitions (tabular + image) to cement intuition
- **Framework:** Get fluent in **PyTorch** (industry standard for AV research; TensorFlow is less common in this space now)

**Milestone:** Train a CNN from scratch on CIFAR-10/MNIST, then fine-tune a pretrained model (ResNet/EfficientNet) on a custom dataset.

---

## PHASE 2 — Computer Vision for Driving (2–3 months)

This is your strongest lane already — push it toward driving-specific tasks.

- **Course:** Stanford **CS231n** (Convolutional Neural Networks for Visual Recognition) — free lecture videos + assignments online
- **Course:** *First Principles of Computer Vision* (Columbia, Coursera) — camera models, epipolar geometry
- **Book:** *Multiple View Geometry in Computer Vision* (Hartley & Zisserman) — the bible for stereo/3D vision, dense but worth having
- **Topics to specifically master:**
  - Object detection: YOLOv8, Faster R-CNN
  - Semantic segmentation: U-Net, DeepLabV3 (for lane/drivable-area segmentation)
  - Multi-object tracking: DeepSORT, ByteTrack
  - Stereo vision & depth estimation
  - Camera calibration (OpenCV's calibration module — you already use OpenCV)

**Milestone:** Build a lane detection + object detection pipeline on dashcam footage (there are free datasets — see Phase 5).

---

## PHASE 3 — Sensor Fusion, SLAM & Localization (2–3 months)

This is where most CS grads have a gap, and where you'll stand out if you fill it.

- **Course:** *State Estimation and Localization for Self-Driving Cars* (Coursera, University of Toronto — part of their **Self-Driving Cars Specialization**, see below)
- **Book:** *Probabilistic Robotics* (Thrun, Burgard, Fox) — the standard reference for Kalman filters, particle filters, SLAM
- **Topics:**
  - Extended Kalman Filter (EKF), Unscented Kalman Filter (UKF)
  - Particle filters
  - Visual SLAM: ORB-SLAM, LIO-SAM (LiDAR-inertial)
  - Point cloud processing: PCL library, PointNet/PointNet++
  - GPS/IMU fusion

**Milestone:** Implement an EKF-based localization system in Python/C++ using a public AV dataset (KITTI has GPS/IMU + camera + LiDAR synced).

---

## PHASE 4 — Prediction, Planning & Control (2–3 months)

This is the decision-making brain of the car.

- **Course:** *Motion Planning for Self-Driving Cars* (Coursera, U. Toronto — same specialization)
- **Course:** *Introduction to Self-Driving Cars* (Coursera, U. Toronto — start of the specialization)
- **Topics:**
  - Path planning: A*, Hybrid A*, RRT/RRT*
  - Trajectory optimization
  - Behavior prediction: LSTMs/Transformers on trajectory data, or simpler Markov models
  - Control: PID, Model Predictive Control (MPC)
  - Decision-making: Finite State Machines, POMDPs (conceptual level is enough unless you go research)

**Milestone:** In CARLA (simulator, see below), get a car to follow a planned path with a PID/MPC controller while avoiding a dynamic obstacle.

---

## PHASE 5 — Full-Stack Integration (ongoing project work)

Now you connect everything into an actual pipeline.

### Simulators (use these — don't wait for a real car)
- **CARLA** — open-source, most widely used AV simulator, Python API, great docs
- **AirSim** (Microsoft) — good alternative, especially for drones/vehicles
- **LGSVL / SVL Simulator** — another strong open option

### Full open-source AV stacks (read the code, don't just use them)
- **Autoware** — full open-source AV software stack, ROS 2-based, huge community
- **Apollo** (Baidu) — production-grade AV stack, well-documented architecture

### Datasets to practice on
- **KITTI** — classic benchmark, stereo + LiDAR + GPS/IMU
- **nuScenes** — large-scale, multi-sensor (camera, LiDAR, radar), great for sensor fusion practice
- **Waymo Open Dataset** — huge, high-quality, industry-grade
- **BDD100K** — diverse dashcam footage, great for detection/segmentation

### Middleware
- **ROS 2** — learn this properly. Nearly every AV research and most production stacks use it or a ROS-like architecture. Official ROS 2 tutorials are free and solid.

**Milestone:** Build a mini end-to-end pipeline in CARLA: camera feed → object/lane detection → simple planner → PID controller driving the simulated car.

---

## Capstone Options (pick one for your portfolio/FYP)

1. **Lane-keeping + obstacle avoidance in CARLA** using your own perception + planning + control stack (most achievable solo).
2. **Sensor fusion project** — fuse camera + LiDAR (simulated or KITTI data) for improved object detection, benchmark against camera-only.
3. **Trajectory prediction model** — given past positions of vehicles/pedestrians (nuScenes), predict future paths using an LSTM/Transformer.
4. Your **AMR (Antimicrobial Resistance) FYP idea is unrelated to this** — if you want to pivot your FYP toward AVs, a sensor-fusion or perception-focused FYP would be a strong, fundable, and portfolio-relevant choice given your CV background.

---

## Career Options

| Role | What it involves | Fits you if... |
|---|---|---|
| **Perception Engineer** | Object detection, segmentation, tracking, sensor fusion | You lean into your CV background — probably your strongest natural fit |
| **Localization/SLAM Engineer** | Kalman filters, SLAM, sensor calibration | You like the math-heavy, precision side |
| **Planning & Controls Engineer** | Path planning, trajectory optimization, control systems | You like robotics/systems thinking, often needs more EE/controls background |
| **ML Infrastructure / MLOps for AV** | Data pipelines, training infra, simulation tooling at scale | You lean toward your full-stack/dev strengths |
| **Simulation Engineer** | Building/maintaining simulators, synthetic data generation, edge-case testing | Overlaps with your software dev + some CV |
| **Research Scientist (AV)** | Novel perception/planning algorithms, usually needs MS/PhD | Long-term path if you go to grad school |
| **Robotics Software Engineer (broader)** | AV skills transfer directly to drones, warehouse robots, agri-robots | Good fallback — AV-specific jobs are geographically concentrated |

### Companies/ecosystem to know
- **Pure AV:** Waymo, Cruise (wound down robotaxi ops in 2024 but tech absorbed into GM), Zoox, Wayve, Mobileye, Aurora, Nuro
- **Automakers with AV divisions:** Tesla (Autopilot/FSD), Rivian, traditional OEMs (Bosch, Continental, ZF as tier-1 suppliers)
- **Chinese AV ecosystem:** Baidu Apollo, Pony.ai, WeRide, XPeng — very active, open-source-friendly (Apollo)
- **Adjacent robotics (good entry point if AV-specific roles are scarce where you are):** warehouse robotics (Amazon Robotics, Locus Robotics), drone companies, agricultural robotics

### Realistic note on geography
Pure AV roles are heavily concentrated in the US (Bay Area, Pittsburgh, Phoenix), China, and parts of Europe/Israel (Mobileye). From Pakistan, the most realistic near-term paths are:
1. Remote-friendly perception/ML roles at AV or robotics companies (rare but exist, especially at smaller/research-heavy teams)
2. Grad school (MS/PhD) abroad specializing in robotics/CV — this is the most common on-ramp people actually use
3. Building a strong open-source/portfolio presence (GitHub, Kaggle, published projects) to get noticed remotely
4. Adjacent robotics/CV roles first, AV specifically later

---

## Future Potential

- AV is not "solved" — Level 4/5 autonomy at scale is still an open, well-funded problem globally. Waymo is scaling robotaxis in more US cities; China's ecosystem (Baidu, Pony.ai, WeRide) is moving fast; Tesla's FSD is iterating aggressively.
- **Perception + sensor fusion remains the hottest sub-field** because it's where deep learning has the most obvious edge, and it transfers directly to robotics, drones, and industrial automation — so skills here are valuable even if pure AV hiring slows in any given year.
- **Simulation and synthetic data** is growing fast as a specialty (real-world edge-case data is expensive/rare; synthetic data generation is a career path of its own).
- Regulatory and safety validation (a mix of ML + systems engineering) is an underrated, growing niche — less flashy, but stable demand.
- Broader robotics (warehouse, agriculture, delivery, drones) is arguably a *safer* long-term bet than pure robotaxi AV, and 80% of the skills overlap.

---

## Do's and Don'ts

### Do
- **Build, don't just watch courses.** A working CARLA pipeline beats 10 completed courses on a resume.
- **Learn ROS/ROS2 early** — it's the connective tissue of almost every real AV/robotics stack, and most CS students skip it.
- **Get comfortable with C++**, even if Python is home base — production AV code is real-time and C++-heavy.
- **Use public datasets (KITTI, nuScenes) to benchmark yourself** against known results — it's how you know if your model is actually good.
- **Document your projects publicly** (GitHub with clear READMEs, maybe a blog) — given the geography issue above, visibility matters more for you than for someone already in Silicon Valley.
- **Study one full open-source stack deeply** (Autoware or Apollo) rather than shallow-skimming many — understanding how perception/planning/control actually talk to each other in a real system is a rare and valuable skill.
- **Go for grad school or research internships** if you're serious about AV specifically — it remains the most reliable on-ramp from outside the major AV hubs.

### Don't
- **Don't skip control theory** thinking "I'm a CS/ML person, not EE" — planning and control roles need it, and even perception engineers benefit from understanding the full loop.
- **Don't over-index on end-to-end deep learning ("just feed pixels, get steering angle")** as if it's the whole field — it's one research direction (Wayve, Comma.ai style) but most production systems are still modular (perception → prediction → planning → control), and understanding the modular approach makes you more hireable broadly.
- **Don't ignore the math** to rush into frameworks — Kalman filters and MPC are debuggable only if you understand what's happening underneath; treating them as black-box library calls will hurt you in interviews and real debugging.
- **Don't assume simulator success = real-world readiness** — sim-to-real gap is a known, serious problem in this field; be aware of it conceptually even if you're simulation-only for now.
- **Don't neglect safety/edge-case thinking** — a huge part of real AV work is about the 1% weird scenarios (occluded pedestrian, sensor failure, adversarial weather), not just the median case. Build this mindset into projects.
- **Don't try to learn everything sequentially before building anything** — you'll stall. Pick the capstone project now, and pull in phases 0–4 topics as the project demands them.

---

## Suggested Order of Attack (given your current standing)

1. **Now–Month 2:** Deep learning fundamentals (Phase 1) + push your CV skills toward detection/segmentation (Phase 2) — this is the shortest path from where you are to something demo-able.
2. **Month 2–4:** Pick up ROS 2 and get CARLA running locally; start a small integration project even before finishing Phase 3/4 in full — motivation follows visible progress.
3. **Month 3–5:** Layer in Kalman filtering/localization (Phase 3) as your project needs it.
4. **Month 4–6:** Planning/control (Phase 4), finish your capstone.
5. **Ongoing:** Decide if AV-specific grad school is the move, or if you pivot toward broader robotics/CV roles with AV as a specialization on your resume.

---

*This is a living roadmap — revisit and adjust every couple of months as you complete milestones. The field moves fast; treat the specific course/tool names above as a starting point, not gospel.*
