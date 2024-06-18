# JavaScript - Web jQuery

`jQuery` - jQuery is a javascript library that helps developers write javascript code more syntatically easily. When combined with ajax, jQuery also helps us update the our website dynamically. In earlier day (i.e during the browser war in the 1990s), jQuery was used to write code that works on all browsers, thus ensuring compatibility. Even today, jQuery let's us write javascript code (such as updating the dom and making ajax request) less verbose compared to vannila javascript.  

## How to use jQuery ?

### Installation
jQuery can be install [locally](https://jquery.com/download/) or use via cdn (content delivery network)

  `jQuery cdn`

  - [google cdn](https://developers.google.com/speed/libraries#jquery)
  - [Microsoft cdn](https://learn.microsoft.com/en-us/aspnet/ajax/cdn/overview#jQuery_Releases_on_the_CDN_0)

### sample how to jQuery

  `via cdn` 
    download one of google cdn or any of you choice and replace the src part with your own link

      <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>

  then add the above line in the head tag of your html page:
  
  like so
    
```<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jquery | JavaScript Library</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
</head>
<body>
    <h1 id="h1">Hello Africa!</h1>
    <p>Welcome to story <span id="africa">Africa</span>!</p>
</body>
</html>```
    
