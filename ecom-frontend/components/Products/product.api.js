const { default: config } = require("components/config");

function getProducts(filters) {
  let url = config.API + "/api/products?";
  for (const key in filters) {
    url += filters[key] != null && filters[key].length > 0 ? `${key}=${filters[key]}&` : "";
  }
  return fetch(url).then(function (res) {
    return res.json();
  }).catch(function (err) {
    console.log(err);
    return [];
  });

}

function getProduct(id) {
  return fetch(config.API + "/api/products/" + id).then(function (res) {
    return res.json();
  }).catch(function (err) {
    console.log(err);
    return {};
  });
}

export { getProducts, getProduct };