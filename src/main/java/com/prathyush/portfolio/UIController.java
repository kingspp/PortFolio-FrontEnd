package com.prathyush.portfolio;

import com.google.gson.GsonBuilder;
import com.prathyush.portfolio.config.Config;
import com.prathyush.portfolio.pojo.User;
import com.prathyush.portfolio.util.ResponsePojo;
import com.prathyush.portfolio.util.UserService;
import spark.Request;
import spark.Spark;

import java.util.List;

/**
 * Created by Prathyush SP on 2/27/2016.
 */
public class UIController {



    public static void main(String args[]){
        Spark.port(9999);
        Spark.staticFileLocation("www");

        Spark.before("/*", (request, response) -> {
            if (request.uri().equals("/")) {
                //System.out.println(request.uri() + " - Is / - Redirecting to index.html");
                response.redirect(request.uri() + "login.html");
                return;
            }
            if (shouldIgnoreRequestFilter(request, new String[]{"css", "js", "images", "login"})) {
                return;
            } else {
                System.out.println(request.uri() + " - Not / - Redirecting to " + request.uri());
                Object userID = request.session().attribute(Config.userSessionKey);
                System.out.println("UserID: " + userID);
                System.out.println("Session ID: " + request.session().id());
                if (userID == null) Spark.halt(401, "You are not welcome here <a href='/login.html'>Login</a><script>window.location.href='/login.html'</script>");
                else
                    return;
            }
        });

        Spark.post("/login", (req, res) -> {
            User u = new User();
            String user = req.queryParams("name");
            String password = req.queryParams("password");
            String status = "Login Failed";
            List<User> list = UserService.getUserList();
            for (User usr : list) {
                if (usr.getName().equals(user) && usr.getPassword().equals(password)) {
                    spark.Session session = req.session(true);
                    session.attribute(Config.userSessionKey, usr.getId());
                    status = "Login Success";
                }
            }
            System.out.println("..");
            ResponsePojo resp = new ResponsePojo();
            resp.setResult(status);
            return new GsonBuilder().create().toJson(resp);
        });

        Spark.get("/get-timeline", (req,res) ->  new GsonBuilder().setPrettyPrinting().create().toJson(TimeLine.getTimeline()));
    }


    public static boolean shouldIgnoreRequestFilter(Request request, String[] ignoreList) {
        for (String i : ignoreList) {
            if (request.uri().toLowerCase().contains(i.toLowerCase())) {
                return true;
            }
        }
        return false;
    }
}
