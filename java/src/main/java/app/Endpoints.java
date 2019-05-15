package app;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.http.ResponseEntity;
import org.springframework.web.client.RestTemplate;
import org.json.JSONObject;

@Controller
public class Endpoints {

    @GetMapping("/index")
    public String greeting(@RequestParam(name="name", required=false, defaultValue="World") String name, Model model) {
        model.addAttribute("name", name);
        return "index";
    }

    @GetMapping("/api")
    @ResponseBody
    public String api() {
        RestTemplate client = new RestTemplate();
        ResponseEntity<String> response = client.getForEntity("https://mars-storm.herokuapp.com/data", String.class);
        JSONObject obj = new JSONObject("{rawData: " + response.getBody() + "}");
        return obj.toString();
    }

}