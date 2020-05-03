# umich.edu.website
Source code for the website hosted on umich.edu/~aidindia. Theme taken from aidnyc.org and header from maryland1.annarbor.org

## How to make changes to a website page?

1. Clone the repository

  ``` shell-session
  $ git clone git@github.com/aidannarbor/umich.edu.website.git
  ```

2. Create a virtual environment

  ```shell-session
  $ make venv/bin/activate
  ```
  
3. Activate the virtual environment

  ```shell-session
  $ source venv/bin/activate
  ```
  
4. If you want to make edits to the events page, make corresponding changes to
   `src/events.jinja`. These changes will be copied to events.html.  After you have made the changes run `make`.
   
   ```shell-session
   $ make
   ```

   This will create some files in the `./build` folder. Checkout the local website as `build/index.html`. Make sure that the changes you made are correct.
   
5. After you are sure that changes look okay. Only then upload them to the server by running 

    ```shell-session
    $ make install USER=<your umich username>
    ```



