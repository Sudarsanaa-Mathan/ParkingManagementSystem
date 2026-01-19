import ParkingApp from "../components/ParkingApp";

export default function AdminDashboard() {
  return (
    <>
    <div>
      <h1>Admin Dashboard</h1>
      <ParkingApp />
      {/* later: slot config, reports, users */}
    </div>
    </>
  );
}
