
package com.prathyush.portfolio.util;



import com.prathyush.portfolio.pojo.User;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by phaneendra on 2/19/16.
 */
public class UserService {
    public static User getUserByID(Integer id){
        List<User> list = getUserList();
        for(User u:list){
            if(u.getId()==id) return u;
        }
        return null;
    }

    public static List<User> getUserList(){
        List<User> list = new ArrayList<>();
        list.add(new User(1,"prathyush-rzt","admin@123"));
        return list;
    }
}
