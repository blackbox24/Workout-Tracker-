# WORKOUT TRACKER PROJECT

This project is a backend system for a workout tracker application where users get to login, signup, create workout plans and track their progress. This will include features like JWT authentication, CRUD operations for workouts and report generations on past workouts

## REQUIREMENTS

- Database Schema
- API endpoints

### Exercise data Schema

- Name
- Description
- category (strength, cardio, flexibility)
- muscle group ( legs, back, chest )

### Authorization and Authentication

- Sign Up: Create an account
- login: Allow users to log into their accounts
- JWT: use JWT for authentication

### WORKOUT MANAGEMENT

- Users create workout plans
- Plans should consist of multiple exercises each with repetitions, sets and weights
- Users delete and update with comments workout plans
- Users schedule workouts for specific dates and times

### PLAN

- [ ] CREATE WORKOUT - Users create workout plans composed of multiple exercises
- [ ] UPDATE WORKOUT - Users update works
- [ ] COMMENT ON WORKOUTS
- [ ] DELETE WORKOUT
- [ ] SCHEDULE WORKOUT
- [ ] LIST WORKOUTS
- [ ] GENERATE REPORTS - Generate reports on past workouts and progress

### CONSTRAINTS

- USE RELATIONAL DB
- USE RESTFUL API
- IMPLEMENT JWT AUTHENTICATION TO SECURE ENDPOINTS
- WRITE UNIT TESTS
- DOCUMENTATION