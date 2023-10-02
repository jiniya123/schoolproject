// dynamic_dropdown.js
//document.addEventListener('DOMContentLoaded', function () {
//    const departmentDropdown = document.getElementById('departmentDropdown');
//    const courseDropdown = document.getElementById('courses');
//
//    departmentDropdown.addEventListener('change', () => {
//        const selectedDepartmentId = departmentDropdown.value;
//
//        for (const option of courseDropdown.options) {
//            const courseDepartmentId = option.getAttribute('data-department');
//            option.style.display = (courseDepartmentId === selectedDepartmentId || courseDepartmentId === '') ? 'block' : 'none';
//        }
//    });
//
//    departmentDropdown.dispatchEvent(new Event('change'));
//});
