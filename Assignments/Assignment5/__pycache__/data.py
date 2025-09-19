from abc import ABC, abstractmethod
from typing import List, Dict, Optional
import uuid
import statistics


# ------------------------
# Base and User classes
# ------------------------

class User(ABC):
    """
    Abstract base class for all users.
    Demonstrates abstraction and encapsulation (protected attributes).
    """
    def _init_(self, name: str, email: str):
        self._id = str(uuid.uuid4())
        self._name = name
        self._email = email

    @property
    def id(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def email(self) -> str:
        return self._email

    @abstractmethod
    def display_info(self) -> None:
        """Polymorphic method implemented by subclasses."""
        pass


class Learner(User):
    """
    Learner subclass. Stores progress and enrolled courses.
    """
    def _init_(self, name: str, email: str):
        super()._init_(name, email)
        self._enrolled_course_ids: List[str] = []
        # progress: course_id -> Progress
        self._progress: Dict[str, "Progress"] = {}

    def enroll(self, course: "Course"):
        if course.id in self._enrolled_course_ids:
            print(f"[Info] Already enrolled in course '{course.title}'.")
            return
        self._enrolled_course_ids.append(course.id)
        self._progress[course.id] = Progress(course.id)
        print(f"[Success] {self.name} enrolled in '{course.title}'.")

    def get_progress(self, course_id: str) -> Optional["Progress"]:
        return self._progress.get(course_id)

    def display_info(self) -> None:
        print(f"Learner: {self.name} (email: {self.email}, id: {self.id})")
        print(" Enrolled courses:", len(self._enrolled_course_ids))

    def list_enrollments(self) -> List[str]:
        return self._enrolled_course_ids


class Instructor(User):
    """
    Instructor subclass. Can own courses.
    """
    def _init_(self, name: str, email: str, bio: str = ""):
        super()._init_(name, email)
        self._bio = bio
        self._course_ids: List[str] = []

    def create_course(self, title: str, language: str, description: str) -> "Course":
        course = Course(title=title, language=language, description=description, instructor_id=self.id)
        self._course_ids.append(course.id)
        print(f"[Success] Course '{title}' created by {self.name}.")
        return course

    def display_info(self) -> None:
        print(f"Instructor: {self.name} (email: {self.email}, id: {self.id})")
        print(f" Bio: {self._bio}")
        print(f" Courses created: {len(self._course_ids)}")

    def list_courses(self) -> List[str]:
        return self._course_ids


# ------------------------
# Supporting domain classes
# ------------------------

class Lesson:
    def _init_(self, title: str, content: str):
        self.id = str(uuid.uuid4())
        self.title = title
        self.content = content

    def display(self):
        print(f"Lesson: {self.title}")
        print(self.content)


class Quiz:
    """
    Simple quiz with multiple-choice questions.
    questions: list of dict { question: str, options: List[str], answer_index: int }
    """
    def _init_(self, title: str):
        self.id = str(uuid.uuid4())
        self.title = title
        self.questions: List[Dict] = []

    def add_question(self, question: str, options: List[str], answer_index: int):
        if answer_index < 0 or answer_index >= len(options):
            raise ValueError("answer_index out of range")
        self.questions.append({
            "question": question,
            "options": options,
            "answer_index": answer_index
        })

    def administer(self) -> float:
        """
        Administer quiz via CLI; returns score percentage (0-100).
        """
        if not self.questions:
            print("[Warning] This quiz has no questions.")
            return 0.0
        print(f"Starting Quiz: {self.title} ({len(self.questions)} questions)")
        correct = 0
        for i, q in enumerate(self.questions, 1):
            print(f"\nQ{i}: {q['question']}")
            for idx, opt in enumerate(q['options']):
                print(f"  {idx}. {opt}")
            # CLI input; if invalid, treat as wrong
            try:
                ans = int(input("Your answer (number): ").strip())
            except Exception:
                ans = -1
            if ans == q['answer_index']:
                print(" -> Correct!")
                correct += 1
            else:
                print(f" -> Wrong. Correct answer: {q['answer_index']}")
        score = correct / len(self.questions) * 100.0
        print(f"\nQuiz complete. Score: {score:.1f}% ({correct}/{len(self.questions)})")
        return score


class Course:
    """
    Course aggregates lessons and quizzes.
    """
    def _init_(self, title: str, language: str, description: str, instructor_id: str):
        self.id = str(uuid.uuid4())
        self.title = title
        self.language = language
        self.description = description
        self.instructor_id = instructor_id
        self.lessons: List[Lesson] = []
        self.quizzes: List[Quiz] = []
        # Class-level tracking example omitted here (see LanguageApp for aggregator)

    def add_lesson(self, lesson: Lesson):
        self.lessons.append(lesson)
        print(f"[Added] Lesson '{lesson.title}' to course '{self.title}'.")

    def add_quiz(self, quiz: Quiz):
        self.quizzes.append(quiz)
        print(f"[Added] Quiz '{quiz.title}' to course '{self.title}'.")

    def display_summary(self):
        print(f"Course: {self.title} ({self.language}) - {self.description}")
        print(f" Instructor id: {self.instructor_id}")
        print(f" Lessons: {len(self.lessons)}, Quizzes: {len(self.quizzes)}")


class Progress:
    """
    Tracks learner progress in a course.
    """
    def _init_(self, course_id: str):
        self.course_id = course_id
        self.lessons_completed: List[str] = []
        self.quiz_scores: List[float] = []

    def complete_lesson(self, lesson_id: str):
        if lesson_id not in self.lessons_completed:
            self.lessons_completed.append(lesson_id)

    def record_quiz_score(self, score: float):
        self.quiz_scores.append(score)

    def completion_rate(self, total_lessons: int) -> float:
        if total_lessons == 0:
            return 0.0
        return len(self.lessons_completed) / total_lessons * 100.0

    def average_quiz_score(self) -> Optional[float]:
        if not self.quiz_scores:
            return None
        return statistics.mean(self.quiz_scores)


# ------------------------
# Manager / Controller
# ------------------------

class LanguageApp:
    """
    Controller class that aggregates users and courses and provides CLI operations.
    Demonstrates class-level attributes and static methods.
    """
    def _init_(self):
        self.learners: Dict[str, Learner] = {}
        self.instructors: Dict[str, Instructor] = {}
        self.courses: Dict[str, Course] = {}

    # --- Registration methods ---
    def register_learner(self, name: str, email: str) -> Learner:
        learner = Learner(name=name, email=email)
        self.learners[learner.id] = learner
        print(f"[Registered] Learner {name} with id {learner.id}")
        return learner

    def register_instructor(self, name: str, email: str, bio: str = "") -> Instructor:
        instr = Instructor(name=name, email=email, bio=bio)
        self.instructors[instr.id] = instr
        print(f"[Registered] Instructor {name} with id {instr.id}")
        return instr

    # --- Course methods ---
    def add_course(self, course: Course):
        self.courses[course.id] = course

    def find_course_by_title(self, title: str) -> Optional[Course]:
        for c in self.courses.values():
            if c.title.lower() == title.lower():
                return c
        return None

    # --- Enrollment & activity ---
    def enroll_learner_to_course(self, learner_id: str, course_id: str):
        learner = self.learners.get(learner_id)
        course = self.courses.get(course_id)
        if not learner:
            print("[Error] Learner not found.")
            return
        if not course:
            print("[Error] Course not found.")
            return
        learner.enroll(course)

    def learner_take_lesson(self, learner_id: str, course_id: str, lesson_index: int):
        learner = self.learners.get(learner_id)
        course = self.courses.get(course_id)
        if not learner or not course:
            print("[Error] Invalid learner or course.")
            return
        if lesson_index < 0 or lesson_index >= len(course.lessons):
            print("[Error] Lesson index out of range.")
            return
        lesson = course.lessons[lesson_index]
        # Display lesson content (could be rich / multimedia in real app)
        lesson.display()
        progress = learner.get_progress(course_id)
        if progress:
            progress.complete_lesson(lesson.id)
            print(f"[Progress] Marked lesson '{lesson.title}' complete for {learner.name}.")

    def learner_take_quiz(self, learner_id: str, course_id: str, quiz_index: int):
        learner = self.learners.get(learner_id)
        course = self.courses.get(course_id)
        if not learner or not course:
            print("[Error] Invalid learner or course.")
            return
        if quiz_index < 0 or quiz_index >= len(course.quizzes):
            print("[Error] Quiz index out of range.")
            return
        quiz = course.quizzes[quiz_index]
        score = quiz.administer()  # CLI interactive
        progress = learner.get_progress(course_id)
        if progress:
            progress.record_quiz_score(score)

    # --- Reports ---
    def course_report(self, course_id: str):
        course = self.courses.get(course_id)
        if not course:
            print("[Error] Course not found.")
            return
        print("=== Course Report ===")
        course.display_summary()
        # Basic aggregated stats from learners
        enrolled = [l for l in self.learners.values() if course_id in l.list_enrollments()]
        print(f" Enrolled learners: {len(enrolled)}")
        avg_completion = []
        avg_quiz_scores = []
        for l in enrolled:
            p = l.get_progress(course_id)
            if p:
                avg_completion.append(p.completion_rate(total_lessons=len(course.lessons)))
                if p.average_quiz_score() is not None:
                    avg_quiz_scores.append(p.average_quiz_score())
        if avg_completion:
            print(f" Avg completion: {statistics.mean(avg_completion):.1f}%")
        else:
            print(" Avg completion: N/A")
        if avg_quiz_scores:
            print(f" Avg quiz score: {statistics.mean(avg_quiz_scores):.1f}%")
        else:
            print(" Avg quiz score: N/A")

    def learner_report(self, learner_id: str):
        learner = self.learners.get(learner_id)
        if not learner:
            print("[Error] Learner not found.")
            return
        print("=== Learner Report ===")
        learner.display_info()
        for course_id in learner.list_enrollments():
            course = self.courses.get(course_id)
            if not course:
                continue
            print(" - Course:", course.title)
            p = learner.get_progress(course_id)
            if p:
                print(f"   Lessons completed: {len(p.lessons_completed)}/{len(course.lessons)}")
                avg = p.average_quiz_score()
                if avg is None:
                    print("   Avg quiz: N/A")
                else:
                    print(f"   Avg quiz: {avg:.1f}%")
        print()

    # Utility to seed some sample data for quick testing
    @staticmethod
    def sample_data(app: "LanguageApp"):
        instr = app.register_instructor("Priya Sharma", "priya@example.com", bio="Experienced Hindi instructor")
        course = instr.create_course(title="Basic Hindi", language="Hindi", description="Beginner course for Hindi")
        app.add_course(course)
        # lessons
        course.add_lesson(Lesson("Introduction", "Welcome to Basic Hindi: alphabet and sounds."))
        course.add_lesson(Lesson("Greetings", "Namaste, Aap kaise ho?"))
        # quiz
        q1 = Quiz("Intro Quiz")
        q1.add_question("How do you say 'hello' in Hindi?", ["Hola", "Namaste", "Bonjour"], 1)
        q1.add_question("What is 'Aap kaise ho?' meaning?", ["How are you?", "What's your name?", "Where are you?"], 0)
        course.add_quiz(q1)
        # learners
        l1 = app.register_learner("Ravi", "ravi@example.com")
        l2 = app.register_learner("Anita", "anita@example.com")
        app.enroll_learner_to_course(l1.id, course.id)
        app.enroll_learner_to_course(l2.id, course.id)
        return app


