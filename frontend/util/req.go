package util

import (
	"io/ioutil"
	"net/http"
	"net/url"
)

const (
	gTree = "https://theinfoseccorner.com/api/genTree"
)

func GetOrg(name string) string {
	// url encode so you can just put in string
	s := url.QueryEscape(name)
	endpoint := gTree + "?user=" + s

	// fmt.Printf(endpoint)
	resp, err := http.Get(endpoint)
	Check(err)

	body, err := ioutil.ReadAll(resp.Body)
	Check(err)

	return string(body)
}
