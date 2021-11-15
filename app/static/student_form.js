function getStudentFormData() {
    formData = $('form').serializeArray();
    studentDataJson = convertStudentDataToJsonOibject(formData);
    submitDataToServer(studentDataJson)
}

function convertStudentDataToJsonOibject(formData) {
    const studentDataObject = {}
    studentDataObject['name'] = formData[0]['value']
    studentDataObject['email_address'] = formData[1]['value']
    studentDataObject['birthday'] = formData[2]['value']
    studentDataObject['subject'] = formData[3]['value']
    jsonStudentDataObject = JSON.stringify(studentDataObject)
    return jsonStudentDataObject
}

function submitDataToServer(studentDataJson) {
    console.log(studentDataJson)
    $.ajax({
        type: 'POST',
        url: "http://localhost:5000/process-student-form-data",
        async: true,
        dataType: 'json',
        contentType:"application/json; charset=utf-8",
        data: studentDataJson,
        success: function(results) {
            console.log(results)
        }});
}

