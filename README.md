# ProjectP
Team project built for the Auxia hackathon.

# Charitam

I think this is going to be kind of relevant to us all, especially these days.

We've developed Charitam, a totally centralised placement-handling tool designed for students and SPCs alike! Gone are the days of annoying Google Forms and hundreds of emails. Charitam's goals is to ensure ease of accessibility, allowing students to create profiles and track their applications. SPCs and campus admins can also manage the hundreds of pouring applications, instead of relying on annoying spreadsheets. 
It rigidly enforces the constraints and eligibility criteria so that SPCs need not manually go through all applicants and check to see if they're eligible.

## Overview

This project implements a backend system for managing student records at an academic institution. The system provides full CRUD (Create, Read, Update, Delete) functionality for student data and ensures data integrity through database constraints such as unique and foreign key constraints. It is built using **FastAPI** as the web framework and **PostgreSQL** as the database.

---

## Features

- **Create Student**: Add new student records with attributes including name, USN, email, date of birth, academic scores, CGPA, backlog status, and department.
- **Read Student**: Retrieve a single student record or a list of students with optional pagination.
- **Update Student**: Modify existing student records while maintaining database integrity.
- **Delete Student**: Remove student records safely from the database.
- **Database Integrity**: Enforces unique constraints on college emails and USNs, and foreign key constraints for department IDs.
- **Health Check Endpoint**: Verify database connectivity and application health.

---

## Technologies

- **FastAPI**: Web framework for building APIs.
- **SQLAlchemy**: Object-relational mapping (ORM) for database interactions.
- **PostgreSQL**: Relational database for persistent storage.
- **Uvicorn**: ASGI server for running the FastAPI application.
