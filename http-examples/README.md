# HTTP call examples for some of the APIs
The http files in this directory contains example requests that can be run using the ["Rest Client" plugin for VS Code](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).

To define the variables create an environments section in the workspace vscode settings (that is in the `.gitignore`) that looks like this (use your own api tokens of course):

```
{
  "rest-client.environmentVariables": {
    "$shared": {},
    "master": {
      "host": "https://master.preprod.stackstate.io",
      "apiToken": "your personal api token"
    },
    "stac-20016": {
      "host": "https://stac-20016.preprod.stackstate.io",
      "apiToken": "your personal api token"
    },    
  }
}
```

Now you can open the `.http` file in VS Code (with the plugin installed). Select the environment in the right bottom of VS Code, and run the requests you want directly from the editor.