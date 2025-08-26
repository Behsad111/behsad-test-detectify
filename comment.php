<!DOCTYPE html>
<html>
<head>
    <title>Comment Posted</title>
</head>
<body>
    <h1>Thank you for your comment!</h1>
    <p>Your comment has been... not really saved, but here it is:</p>
    
    <!-- This is the vulnerable part -->
    <p><strong>
        <script>
            const queryString = window.location.search;
            const urlParams = new URLSearchParams(queryString);
            const comment = urlParams.get('comment');
            document.write(comment); // This is where the XSS happens!
        </script>
    </strong></p>

    <a href="index.html">Back to home</a>
</body>
</html>
