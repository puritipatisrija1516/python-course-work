def main_cli():
    app = LanguageApp()
    LanguageApp.sample_data(app)  # seed some sample data for quick start

    menu = """
--- Language Learning App CLI ---
1. List courses
2. Create instructor
3. Create course (as instructor)
4. Register learner
5. Enroll learner in course
6. List learners & instructors
7. Take lesson
8. Take quiz
9. Course report
10. Learner report
0. Exit
Choose an option: """

    while True:
        try:
            choice = input(menu).strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            break

        if choice == "0":
            print("Goodbye.")
            break
        elif choice == "1":
            if not app.courses:
                print("No courses yet.")
            else:
                for c in app.courses.values():
                    c.display_summary()
        elif choice == "2":
            name = input("Instructor name: ").strip()
            email = input("Email: ").strip()
            bio = input("Short bio (optional): ").strip()
            app.register_instructor(name, email, bio)
        elif choice == "3":
            instr_id = input("Instructor id: ").strip()
            instr = app.instructors.get(instr_id)
            if not instr:
                print("Instructor not found. List instructors to get ids.")
                continue
            title = input("Course title: ").strip()
            lang = input("Language: ").strip()
            desc = input("Description: ").strip()
            course = instr.create_course(title, lang, desc)
            app.add_course(course)
            # optionally add a lesson/quiz immediately
            add_more = input("Add a lesson now? (y/n): ").strip().lower()
            if add_more == "y":
                lt = input("Lesson title: ").strip()
                lc = input("Lesson content: ").strip()
                course.add_lesson(Lesson(lt, lc))
        elif choice == "4":
            name = input("Learner name: ").strip()
            email = input("Email: ").strip()
            app.register_learner(name, email)
        elif choice == "5":
            learner_id = input("Learner id: ").strip()
            course_id = input("Course id: ").strip()
            app.enroll_learner_to_course(learner_id, course_id)
        elif choice == "6":
            print("Instructors:")
            for i in app.instructors.values():
                print(f"  {i.id} - {i.name} ({i.email})")
            print("Learners:")
            for l in app.learners.values():
                print(f"  {l.id} - {l.name} ({l.email})")
        elif choice == "7":
            learner_id = input("Learner id: ").strip()
            course_id = input("Course id: ").strip()
            course = app.courses.get(course_id)
            if not course:
                print("Course not found.")
                continue
            if not course.lessons:
                print("No lessons in this course.")
                continue
            print("Lessons:")
            for idx, lesson in enumerate(course.lessons):
                print(f" {idx}. {lesson.title}")
            try:
                li = int(input("Lesson index to take: ").strip())
            except Exception:
                print("Invalid index.")
                continue
            app.learner_take_lesson(learner_id, course_id, li)
        elif choice == "8":
            learner_id = input("Learner id: ").strip()
            course_id = input("Course id: ").strip()
            course = app.courses.get(course_id)
            if not course:
                print("Course not found.")
                continue
            if not course.quizzes:
                print("No quizzes in this course.")
                continue
            print("Quizzes:")
            for idx, quiz in enumerate(course.quizzes):
                print(f" {idx}. {quiz.title}")
            try:
                qi = int(input("Quiz index to take: ").strip())
            except Exception:
                print("Invalid index.")
                continue
            app.learner_take_quiz(learner_id, course_id, qi)
        elif choice == "9":
            course_id = input("Course id: ").strip()
            app.course_report(course_id)
        elif choice == "10":
            learner_id = input("Learner id: ").strip()
            app.learner_report(learner_id)
        else:
            print("Unknown option. Try again.")

if __name__ == "_main_":
    main_cli()