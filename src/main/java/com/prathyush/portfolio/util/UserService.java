
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
        list.add(new User(1,"amith","amith"));
        list.add(new User(2,"phani","phani"));
        list.add(new User(3,"nandu","nandu"));
        list.add(new User(4,"shams","shams"));
        list.add(new User(5,"dey","dey"));
        list.add(new User(6,"hima","hima"));
        list.add(new User(7,"vasuki","vasuki"));
        list.add(new User(8,"pratyush","pratyush"));
        list.add(new User(8,"admin","admin"));
        list.add(new User(8,"admin1","admin1"));
        list.add(new User(8,"avinash","avinash"));

        return list;
    }
}
