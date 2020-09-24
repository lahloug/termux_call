This small python library is meant to be installed within an android phone to make phone calls in a terminal. 


Requirements
-------------

Within your android phone:

* Install F-droid directly on their website: https://www.f-droid.org/
* Activate the archive repository option on the know repositories menu
* Download the latest version of termux
* Download termux-api (latest version which gives access to both sms and call api)

Once you open the termux application, run on the terminal:

```
  $ pkg update
  $ pkg upgrade
  $ pkg install termux-api
  $ git clone https://github.com/lahloug/termux_call.git
  $ cd termux_call
  $ pip install -e .
  $ echo 'eval "$(register-python-argcomplete termux-call)"' >> ~/.bashrc
```

Now, you can call anyone on your contact book from your terminal!

```
 $ termux-call person_name
```

Beware, phone charges incur as usual.
