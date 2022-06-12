var test_content = "onclick test content"

function experience() {
    document.getElementsByClassName("summary").innerHTML = "Test";
}

function generatePDF() {
    console.log("Button clicked!")
    // Choose the element that our invoice is rendered in.
    const element = document.getElementById('profile_content');
    console.log(element)
    // Choose the element and save the PDF for our user.
    html2pdf().from(element).save();
}