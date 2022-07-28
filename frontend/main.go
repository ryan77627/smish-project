package main

import (
	"encoding/json"
	"fmt"
	"html/template"
	"net/http"
	"strconv"

	util "github.com/ryan77627/smish-project/frontend/util"
)

const (
	PORT = 8080
	TPL  = "template/*.html"
)

type Hierarchy struct {
	Name      string   `json:"name"`
	Employees []string `json:"employees"`
}

type Full struct {
	Sidebar  Side
	Network  Net
	Bargraph Bar
}

type Side struct {
	Navs []string
}

type Bar struct {
	Hi string
}

type Net struct {
	Hi string
}

func root(w http.ResponseWriter, r *http.Request) {
	tpl := template.Must(template.ParseGlob(TPL))
	tpl.ExecuteTemplate(w, "preview", nil)
}

func console(w http.ResponseWriter, r *http.Request) {
	tpl := template.Must(template.ParseGlob(TPL))

	var campaigns map[string][]string

	fmt.Printf("%v", util.GetCampaigns())

	err := json.Unmarshal([]byte(util.GetCampaigns()), &campaigns)
	util.Check(err)

	// fmt.Printf(util.GetCampaignDetails())

	// var thierarhy Hierarchy

	// test := util.GetOrg("Kristy Preston")

	// err := json.Unmarshal([]byte(test), &thierarhy)
	// util.Check(err)

	// fmt.Printf("%s", thierarhy.Name)
	// fmt.Printf("%d", len(thierarhy.Employees))

	full := Full{
		Sidebar: Side{
			Navs: []string{"Home", "Dashboard"},
		},
		Network:  Net{Hi: "asdfsa"},
		Bargraph: Bar{Hi: "asdj"},
	}
	// full := Full.Sidebar
	tpl.ExecuteTemplate(w, "admin-console", full)

}

func preview(w http.ResponseWriter, r *http.Request) {
	tpl := template.Must(template.ParseGlob(TPL))
	tpl.ExecuteTemplate(w, "preview", nil)
}

func main() {
	port := strconv.Itoa(PORT)

	http.HandleFunc("/", root)
	http.HandleFunc("/console", console)
	http.HandleFunc("/preview", preview)

	fmt.Printf("Running on\nhttp://localhost:%s\n", port)

	util.Check(http.ListenAndServe(":"+port, nil))

}
