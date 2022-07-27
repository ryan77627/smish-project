package main

import (
	"fmt"
	"net/http"
	"strconv"
	"text/template"

	util "github.com/ryan77627/smish-project/frontend/util"
)

const (
	PORT = 8080
	TPL  = "template/*.html"
)

func root(w http.ResponseWriter, r *http.Request) {
	tpl := template.Must(template.ParseGlob(TPL))
	tpl.ExecuteTemplate(w, "main", nil)
}

func console(w http.ResponseWriter, r *http.Request) {
	tpl := template.Must(template.ParseGlob(TPL))
	tpl.ExecuteTemplate(w, "admin-console", nil)
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
