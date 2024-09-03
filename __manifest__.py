{
    'name': 'School Management',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Manage student details and enrollment',
    'author': 'Vastav Taneja',
    # 'website': 'https://yourwebsite.com',
    'depends': ['base'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'data/school.subject.csv',
        'data/school.studentclass.xml',
        'data/school.student.xml',
        'views/student_view.xml',    # Add student views first
        'views/class_view.xml',      # Then class views
        'views/subject_view.xml',    # Then subject views
        'views/teacher_view.xml',    # Then teacher views
        'views/event_view.xml',      # Then event view
        'views/student_grade_view.xml',
        'views/menu.xml',            # Menu views last
    ],
    'installable': True,
    'application': True,
}
